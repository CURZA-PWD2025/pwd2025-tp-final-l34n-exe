from ...database.conect_db import ConectDB
from ..venta.venta_model import VentaModel as Venta
from ..producto.producto_model import ProductoModel as Producto

class ItemVentaModel:
    def __init__(self, id:int=0, cantidad:int=0, venta:Venta=None, producto:Producto=None):
        self.id = id
        self.cantidad = cantidad
        self.venta = venta
        self.producto = producto

    def serializar(self)->dict:
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "venta": self.venta.serializar() if self.venta else None,
            "producto": self.producto.serializar() if self.producto else None
        }

    @staticmethod
    def deserializar(data:dict) -> 'ItemVentaModel':
        return ItemVentaModel(
            id=data["id"],
            cantidad=data["cantidad"],
            venta=Venta.deserializar(data["venta"]) if "venta" in data and data["venta"] else None,
            producto=Producto.deserializar(data["producto"]) if data["producto"] else None,
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas")
                rows = cursor.fetchall()
                items_venta = []
                for row in rows:
                    row["producto"] = Producto.get_by_id(row["id_producto"])
                    del row["id_producto"]
                    row["venta"] = Venta.get_by_id(row["id_venta"])
                    del row["id_venta"]
                    items_venta.append(row)
                return items_venta
            except Exception as exc:
                print(f"Error:{exc}")
                return []
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas WHERE id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    row["producto"] = Producto.get_by_id(row["id_producto"])
                    del row["id_producto"]
                    row["venta"] = Venta.get_by_id(row["id_venta"])
                    del row["id_venta"]
                return row
            except Exception as exc:
                print(f"Error:{exc}")
                return []
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute(
                    "INSERT INTO items_ventas (cantidad, id_venta, id_producto) VALUES (%s, %s, %s)",
                    (self.cantidad,
                     self.venta.id if self.venta else None,
                     self.producto.id if self.producto else None)
                )
                cnx.commit()
                self.id = cursor.lastrowid
                return True
            except Exception as exc:
                print(f"Error:{exc}")
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "UPDATE items_ventas SET cantidad=%s, id_venta=%s, id_producto=%s WHERE id=%s",
                    (self.cantidad,
                     self.venta.id if self.venta else None,
                     self.producto.id if self.producto else None,
                     self.id)
                )
                cnx.commit()
                return True
            except Exception as exc:
                print(f"Error:{exc}")
                return False
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM items_ventas WHERE id=%s", (self.id,))
                cnx.commit()
                return True
            except Exception as exc:
                print(f"Error:{exc}")
                return False
            finally:
                cnx.close()