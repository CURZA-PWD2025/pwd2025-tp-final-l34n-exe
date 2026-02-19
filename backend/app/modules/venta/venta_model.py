from ...database.conect_db import ConectDB
from ..cliente.cliente_model import ClienteModel as Cliente
from ..empleado.empleado_model import EmpleadoModel as Empleado

class VentaModel:
    def __init__(self, id: int = 0, fecha: str = "", total: float = 0.0, estado: str = "abierta", cliente: Cliente = None, empleado: Empleado = None):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.estado = estado
        self.cliente = cliente
        self.empleado = empleado

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "fecha": self.fecha,
            "total": self.total,
            "estado": self.estado,
            "cliente": self.cliente.serializar() if self.cliente else None,
            "empleado": self.empleado.serializar() if self.empleado else None,
        }

    @staticmethod
    def deserializar(data: dict) -> "VentaModel":
        return VentaModel(
            id=data["id"],
            fecha=data["fecha"],
            total=data["total"],
            estado=data["estado"],
            cliente=Cliente.deserializar(data["cliente"]) if data.get("cliente") else None,
            empleado=Empleado.deserializar(data["empleado"]) if data.get("empleado") else None,
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM ventas")
                rows = cursor.fetchall()

                ventas = []
                for row in rows:
                    row["cliente"] = Cliente.get_by_id(row["id_cliente"])
                    row["empleado"] = Empleado.get_by_id(row["id_empleado"])
                    del row["id_cliente"]
                    del row["id_empleado"]
                    ventas.append(row)

                return ventas
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id: int) -> dict | None:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM ventas WHERE id=%s", (id,))
                venta = cursor.fetchone()
                if not venta:
                    return None

                venta["cliente"] = Cliente.get_by_id(venta["id_cliente"])
                venta["empleado"] = Empleado.get_by_id(venta["id_empleado"])
                del venta["id_cliente"]
                del venta["id_empleado"]

                return venta
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                # Total y estado siempre van a estar por defecto al crear en 0 y "abierta" ya que luego se actualizan.
                cursor.execute(
                    """
                    INSERT INTO ventas (fecha, total, estado, id_cliente, id_empleado)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        self.fecha,
                        0,
                        "abierta",
                        self.cliente.id,
                        self.empleado.id,
                    ),
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return True

            except Exception as exc:
                cnx.rollback()
                print(f"Error al crear venta: {exc}")
                return False

            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        cursor = cnx.cursor(dictionary=True)

        try:
            # Bloqueo de la venta
            cursor.execute(
                "SELECT estado FROM ventas WHERE id=%s FOR UPDATE",
                (self.id,),
            )
            venta_db = cursor.fetchone()
            # Verifico existencia
            if not venta_db:
                raise Exception("La venta no existe")
            # Lo nombro estado_anterior porque es más claro luego en el código abajo cuando hago las validaciones de estado
            estado_anterior = venta_db["estado"]

            #  Validaciones de estado
            if estado_anterior == "cerrada" and self.estado == "cerrada":
                raise Exception("La venta ya está cerrada")

            # Cierre de venta
            if estado_anterior == "abierta" and self.estado == "cerrada":
                self.cerrar_venta(cursor)
                cnx.commit()
                return True

            # Update normal (venta abierta)
            cursor.execute(
                """
                UPDATE ventas
                SET fecha=%s,
                    estado=%s,
                    id_cliente=%s,
                    id_empleado=%s
                WHERE id=%s
                """,
                (
                    self.fecha,
                    self.estado,
                    self.cliente.id,
                    self.empleado.id,
                    self.id,
                ),
            )

            cnx.commit()
            return True

        except Exception as exc:
            cnx.rollback()
            print(f"Error al actualizar venta: {exc}")
            return False

        finally:
            cursor.close()
            cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                # Verifico que la venta exista y que no esté cerrada antes de eliminarla
                cursor.execute("SELECT estado FROM ventas WHERE id=%s", (self.id,))
                row = cursor.fetchone()
                # Verifico existencia
                if not row:
                    raise Exception("La venta no existe")
                # Verifico estado
                if row["estado"] == "cerrada":
                    raise Exception("No se puede eliminar una venta cerrada")
                # Elimino la venta
                cursor.execute("DELETE FROM ventas WHERE id=%s", (self.id,))
                cnx.commit()
                return True

            except Exception as exc:
                cnx.rollback()
                print(f"Error al eliminar venta: {exc}")
                return False

            finally:
                cnx.close()

    def cerrar_venta(self, cursor):
        # Verificar ítems
        cursor.execute(
            "SELECT COUNT(*) AS cantidad FROM items_ventas WHERE id_venta=%s",
            (self.id,),
        )
        if cursor.fetchone()["cantidad"] == 0:
            raise Exception("No se puede cerrar una venta sin ítems")

        # Validar sabores obligatorios
        cursor.execute(
            """
            SELECT
                i.id AS id_item,
                p.nombre,
                p.max_sabores,
                COUNT(ivs.id_sabor) AS sabores_cargados
            FROM items_ventas i
            JOIN productos p ON p.id = i.id_producto
            LEFT JOIN items_venta_sabores ivs ON ivs.id_item = i.id
            WHERE i.id_venta = %s
            GROUP BY i.id, p.max_sabores
            """,
            (self.id,),
        )
        # Recorro los items y verifico si alguno requiere sabores pero no tiene
        for item in cursor.fetchall():
            if item["max_sabores"] > 0 and item["sabores_cargados"] == 0:
                raise Exception(
                    f"El item '{item['nombre']}' requiere sabores y no tiene ninguno asignado"
                )

        # Actualizo los subtotales de los items con precios actuales
        cursor.execute(
            """
            UPDATE items_ventas
            SET subtotal = cantidad * (
                SELECT precio 
                FROM productos 
                WHERE id = items_ventas.id_producto
            )
            WHERE id_venta = %s
            """,
            (self.id,),
        )
        
        # Actualizo el total de la venta usando precios actuales de productos
        cursor.execute(
            """
            UPDATE ventas
            SET total = (
                SELECT COALESCE(SUM(iv.cantidad * p.precio), 0)
                FROM items_ventas iv
                JOIN productos p ON p.id = iv.id_producto
                WHERE iv.id_venta = %s
            )
            WHERE id = %s
            """,
            (self.id, self.id),
        )
        # Obtengo los items de la venta para descontar stock
        cursor.execute(
            """
            SELECT id, id_producto, cantidad
            FROM items_ventas
            WHERE id_venta=%s
            """,
            (self.id,),
        )
        items = cursor.fetchall()

        # Recorro los items para descontar stock
        for item in items:
            cursor.execute(
                """
                UPDATE productos
                SET stock = stock - %s,
                    disponible = IF(stock - %s > 0, 1, 0)
                WHERE id=%s AND stock >= %s
                """,
                (
                    item["cantidad"],
                    item["cantidad"],
                    item["id_producto"],
                    item["cantidad"],
                ),
            )
            if cursor.rowcount == 0:
                raise Exception("Stock insuficiente de producto")

            # Obtengo los sabores asociados al item
            cursor.execute(
                "SELECT id_sabor FROM items_venta_sabores WHERE id_item=%s",
                (item["id"],),
            )
            # Recorro los sabores asociados al item para descontar stock
            for sabor in cursor.fetchall():
                cursor.execute(
                    """
                    UPDATE sabores
                    SET stock = stock - %s,
                        disponible = IF(stock - %s > 0, 1, 0)
                    WHERE id=%s AND stock >= %s
                    """,
                    (
                        item["cantidad"],
                        item["cantidad"],
                        sabor["id_sabor"],
                        item["cantidad"],
                    ),
                )
                if cursor.rowcount == 0:
                    raise Exception("Stock insuficiente de sabor")

        # CIERRE DEFINITIVO
        cursor.execute(
            "UPDATE ventas SET estado='cerrada' WHERE id=%s",
            (self.id,),
        )
