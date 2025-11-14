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
            except Exception as exc:
                return {"mensaje":f"Error al obtener las ventas:{exc}"}
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
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
                return venta
            except Exception as exc:
                return {"mensaje":f"Error al obtener la venta:{exc}"}
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO ventas (fecha, total, id_cliente, id_empleado) VALUES (%s, %s, %s, %s)", (self.fecha, self.total, self.cliente.id, self.empleado.id))
                self.id = cursor.lastrowid
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print ({"mensaje": f"Error al crear la venta: {exc}"})
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE ventas SET fecha=%s, total=%s, id_cliente=%s, id_empleado=%s WHERE id=%s", (self.fecha, self.total, self.cliente.id, self.empleado.id, self.id))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al actualizar la venta: {exc}"})
                return False
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM ventas WHERE id=%s", (self.id,))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al eliminar la venta: {exc}"})
                return False
            finally:
                cnx.close()
