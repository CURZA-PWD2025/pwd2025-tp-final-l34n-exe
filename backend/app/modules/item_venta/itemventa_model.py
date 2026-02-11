from ...database.conect_db import ConectDB
from ..venta.venta_model import VentaModel as Venta
from ..producto.producto_model import ProductoModel as Producto


class ItemVentaModel:
    def __init__(
        self,
        id: int = 0,
        cantidad: int = 0,
        venta: Venta = None,
        producto: Producto = None,
    ):
        self.id = id
        self.cantidad = cantidad
        self.venta = venta
        self.producto = producto


    def serializar(self) -> dict:
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "venta": self.venta.serializar() if self.venta else None,
            "producto": self.producto.serializar() if self.producto else None,
        }

    @staticmethod
    def deserializar(data: dict) -> "ItemVentaModel":
        return ItemVentaModel(
            id=data["id"],
            cantidad=data["cantidad"],
            venta=Venta.deserializar(data["venta"]) if data.get("venta") else None,
            producto=Producto.deserializar(data["producto"]) if data.get("producto") else None,
        )


    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas")
                rows = cursor.fetchall()

                items = []
                for row in rows:
                    row["producto"] = Producto.get_by_id(row["id_producto"])
                    row["venta"] = Venta.get_by_id(row["id_venta"])
                    del row["id_producto"]
                    del row["id_venta"]
                    items.append(row)

                return items
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id: int) -> dict | None:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas WHERE id=%s", (id,))
                row = cursor.fetchone()
                if not row:
                    return None

                row["producto"] = Producto.get_by_id(row["id_producto"])
                row["venta"] = Venta.get_by_id(row["id_venta"])
                del row["id_producto"]
                del row["id_venta"]

                return row
            finally:
                cnx.close()


    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #  No permitir items en venta cerrada
                cursor.execute(
                    "SELECT estado FROM ventas WHERE id=%s",
                    (self.venta.id,),
                )
                venta = cursor.fetchone()
                if not venta:
                    raise Exception("La venta no existe")

                if venta["estado"] == "cerrada":
                    raise Exception("No se pueden agregar ítems a una venta cerrada")

                # Precio actual
                cursor.execute(
                    "SELECT precio FROM productos WHERE id=%s",
                    (self.producto.id,),
                )
                producto = cursor.fetchone()
                if not producto:
                    raise Exception("Producto inexistente")

                subtotal = float(producto["precio"]) * float(self.cantidad)

                cursor.execute(
                    """
                    INSERT INTO items_ventas (id_venta, id_producto, cantidad, subtotal)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        self.venta.id,
                        self.producto.id,
                        self.cantidad,
                        subtotal,
                    ),
                )
                cnx.commit()
                return True

            except Exception as exc:
                cnx.rollback()
                print(f"Error al crear item de venta: {exc}")
                return False

            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #  Verificar estado de venta
                cursor.execute(
                    """
                    SELECT v.estado
                    FROM ventas v
                    JOIN items_ventas i ON i.id_venta = v.id
                    WHERE i.id=%s
                    """,
                    (self.id,),
                )
                venta = cursor.fetchone()
                # Verifico existencia
                if not venta:
                    raise Exception("Item o venta inexistente")
                # Verifico estado y si es cerrada no permito modificar el item
                if venta["estado"] == "cerrada":
                    raise Exception("No se pueden modificar ítems de una venta cerrada")

                #  Precio actual
                cursor.execute(
                    "SELECT precio FROM productos WHERE id=%s",
                    (self.producto.id,),
                )
                # Obtengo el producto para luego calcular el subtotal con el precio actual
                producto = cursor.fetchone()
                # Verifico existencia del producto
                if not producto:
                    raise Exception("Producto inexistente")
                # Calculo el subtotal con el precio actual del producto y la cantidad de items
                subtotal = float(producto["precio"]) * float(self.cantidad)
                # Actualizo el item con el nuevo producto, cantidad y subtotal
                cursor.execute(
                    """
                    UPDATE items_ventas
                    SET id_producto=%s,
                        cantidad=%s,
                        subtotal=%s
                    WHERE id=%s
                    """,
                    (
                        self.producto.id,
                        self.cantidad,
                        subtotal,
                        self.id,
                    ),
                )
                cnx.commit()
                return True

            except Exception as exc:
                cnx.rollback()
                print(f"Error al actualizar item de venta: {exc}")
                return False

            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                #  Verificar estado de venta
                cursor.execute(
                    """
                    SELECT v.estado
                    FROM ventas v
                    JOIN items_ventas i ON i.id_venta = v.id
                    WHERE i.id=%s
                    """,
                    (self.id,),
                )
                # Verifico existencia
                venta = cursor.fetchone()
                if not venta:
                    raise Exception("Item o venta inexistente")
                # Verifico estado y si es cerrada no permito eliminar el item
                if venta["estado"] == "cerrada":
                    raise Exception("No se pueden eliminar ítems de una venta cerrada")
                # Obtengo el id de la ventaa para luego eliminar el item
                cursor.execute("SELECT id_venta FROM items_ventas WHERE id=%s", (self.id,))
                id_venta = cursor.fetchone()["id_venta"]
                # Elimino el item
                cursor.execute(
                    "DELETE FROM items_ventas WHERE id=%s",
                    (self.id,),
                )
                cnx.commit()
                return True

            except Exception as exc:
                cnx.rollback()
                print(f"Error al eliminar item de venta: {exc}")
                return False

            finally:
                cnx.close()
