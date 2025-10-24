from ...database.conect_db import ConectDB
from ..cliente.cliente_model import ClienteModel as Cliente
from ..empleado.empleado_model import EmpleadoModel as Empleado
from ..producto.producto_model import ProductoModel as Producto


class VentaModel:
    def __init__(self, id:int=0, fecha:str="", total:float=0.0, cliente:Cliente=None, empleado:Empleado=None):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.cliente = cliente
        self.empleado = empleado

    def serializar(self)->dict:
        return {
            "id": self.id,
            "fecha": self.fecha,
            "total": self.total,
            "cliente": self.cliente.serializar() if self.cliente else None,
            "empleado": self.empleado.serializar() if self.empleado else None
        }

    @staticmethod
    def deserializar(data:dict) -> 'VentaModel':
        return VentaModel(
            id=data["id"],
            fecha=data["fecha"],
            total=data["total"],
            cliente=Cliente.deserializar(data["cliente"]) if data["cliente"] else None,
            empleado=Empleado.deserializar(data["empleado"]) if data["empleado"] else None
        )

    @staticmethod
    def get_all() -> list[dict]:
        from ..item_venta.itemventa_model import ItemVentaModel as ItemVenta
        from ..itemventa_sabor.itemventasabor_model import ItemVentaSaborModel as ItemVentaSabor
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM ventas")
                ventas = cursor.fetchall()

                for venta in ventas:
                    venta["cliente"] = Cliente.get_by_id(venta["id_cliente"])
                    venta["empleado"] = Empleado.get_by_id(venta["id_empleado"])
                    del venta["id_cliente"]
                    del venta["id_empleado"]
                    cursor.execute("SELECT * FROM items_ventas WHERE id_venta = %s", (venta["id"],))
                    items = cursor.fetchall()

                    for item in items:
                        item["producto"] = Producto.get_by_id(item["id_producto"])
                        del item["id_producto"]
                        item["sabores"] = ItemVentaSabor.get_by_item_id(item["id"])
                    venta["items"] = items
                return ventas

            except Exception as exc:
                print(f"Error:{exc}")
                return []
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        from ..item_venta.itemventa_model import ItemVentaModel as ItemVenta
        from ..itemventa_sabor.itemventasabor_model import ItemVentaSaborModel as ItemVentaSabor
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM ventas where id=%s", (id,))
                venta = cursor.fetchone()
                if not venta:
                    return None
                venta["cliente"] = Cliente.get_by_id(venta["id_cliente"])
                venta["empleado"] = Empleado.get_by_id(venta["id_empleado"])
                del venta["id_cliente"]
                del venta["id_empleado"]
                venta["items"] = ItemVenta.get_by_venta_id(id)

                return venta

            except Exception as exc:
                return (f"Error:{exc}")
            finally:
                cnx.close()

    def create(self) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO ventas (fecha, total, id_cliente, id_empleado) VALUES (%s, %s, %s, %s)", (self.fecha, self.total, self.cliente.id, self.empleado.id))
                self.id = cursor.lastrowid
                cnx.commit()
                return True
            except Exception as exc:
                cnx.rollback()
                return ({"mensaje": f"Error al crear la venta: {exc}"})
            finally:
                cnx.close()

    def update(self) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE ventas SET fecha=%s, total=%s WHERE id=%s", (self.fecha, self.total, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar la venta: {exc}"}
            finally:
                cnx.close()

    def delete(self) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM ventas WHERE id=%s", (self.id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al eliminar la venta: {exc}"}
            finally:
                cnx.close()
