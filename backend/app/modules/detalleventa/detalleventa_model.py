from ..database.conect_db import ConectDB
from ..producto.producto_model import ProductoModel as Producto
from ..venta.venta_model import VentaModel as Venta

class DetalleVentaModel:
    def __init__(self, id_venta:int=0, id_producto:int=0, cantidad:int=0, precio_unitario:float=0.0):
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def serializar(self) -> dict:
        return {
            "id_venta": self.id_venta,
            "id_producto": self.id_producto,
            "cantidad": self.cantidad,
            "precio_unitario": self.precio_unitario
        }

    @staticmethod
    def deserializar(data: dict):
        return DetalleVentaModel(
            id_venta=data["id_venta"],
            id_producto=data["id_producto"],
            cantidad=data["cantidad"],
            precio_unitario=data["precio_unitario"]
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM detalle_venta")
                rows = cursor.fetchall()
                detalles_venta = []
                if rows:
                    for row in rows:
                        venta = Venta.get_by_id(row['id_venta'])
                        producto = Producto.get_by_id(row['id_producto'])
                        row["venta"] = venta
                        row["producto"] = producto
                        detalles_venta.append(row)
                return detalles_venta
            except Exception as exc:
                print(f"Error: {exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id_venta: int, id_producto: int):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "SELECT * FROM detalle_venta WHERE id_venta=%s AND id_producto=%s",
                    (id_venta, id_producto)
                )
                row = cursor.fetchone()
                if row:
                    venta = Venta.get_by_id(row['id_venta'])
                    producto = Producto.get_by_id(row['id_producto'])
                    row["venta"] = venta
                    row["producto"] = producto
                    return row
                return None
            except Exception as exc:
                print(f"Error: {exc}")
                return None
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                    (self.id_venta, self.id_producto, self.cantidad, self.precio_unitario)
                )
                result = cursor.rowcount
                cnx.commit()
                return result > 0
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el detalle de la venta: {exc}"}
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "UPDATE detalle_venta SET cantidad=%s, precio_unitario=%s WHERE id_venta=%s AND id_producto=%s",
                    (self.cantidad, self.precio_unitario, self.id_venta, self.id_producto)
                )
                result = cursor.rowcount
                cnx.commit()
                return result > 0
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el detalle: {exc}"}
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute(
                    "DELETE FROM detalle_venta WHERE id_venta=%s AND id_producto=%s",
                    (self.id_venta, self.id_producto)
                )
                result = cursor.rowcount
                cnx.commit()
                return result > 0
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al eliminar el detalle de la venta: {exc}"}
            finally:
                cnx.close()
