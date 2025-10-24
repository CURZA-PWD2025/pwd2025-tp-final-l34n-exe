from ...database.conect_db import ConectDB
from ..venta.venta_model import VentaModel as Venta
from ..producto.producto_model import ProductoModel as Producto


class ItemVentaModel:
    def __init__(self, id:int=0, cantidad:int=0, venta:Venta=None, producto:Producto=None, sabores:list=None):
        self.id = id
        self.cantidad = cantidad
        self.venta = venta
        self.producto = producto
        self.sabores = []

    def serializar(self)->dict:
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "venta": self.venta.serializar() if self.venta else None,
            "producto": self.producto.serializar() if self.producto else None,
            "sabores": self.sabores
        }

    @staticmethod
    def deserializar(data:dict) -> 'ItemVentaModel':
        return ItemVentaModel(
            id=data["id"],
            cantidad=data["cantidad"],
            venta=Venta.deserializar(data["venta"]) if "venta" in data and data["venta"] else None,
            producto=Producto.deserializar(data["producto"]) if data["producto"] else None,
            sabores=data["sabores"]
        )


    @staticmethod
    def get_all() -> list[dict]:
        from ..itemventa_sabor.itemventasabor_model import ItemVentaSaborModel as ItemVentaSabor
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas")
                rows = cursor.fetchall()
                items_venta = []
                for row in rows:
                    item = dict(row)
                    item["sabores"] = ItemVentaSabor.get_by_item_id(row["id"])
                    items_venta.append(item)
                return items_venta
            except Exception as exc:
                print(f"Error:{exc}")
                return []
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        from ..itemventa_sabor.itemventasabor_model import ItemVentaSaborModel as ItemVentaSabor
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas WHERE id=%s", (id,))
                item_venta = cursor.fetchone()
                if item_venta:
                    item_venta["producto"] = Producto.get_by_id(item_venta["id_producto"])
                    del item_venta["id_producto"]
                    item_venta["sabores"] = ItemVentaSabor.get_by_item_id(item_venta["id"])
                return item_venta
            except Exception as exc:
                print(f"Error:{exc}")
                return None
            finally:
                cnx.close()

    @staticmethod
    def get_by_venta_id(id_venta:int) -> dict:
        from ..itemventa_sabor.itemventasabor_model import ItemVentaSaborModel as ItemVentaSabor
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_ventas WHERE id_venta = %s", (id_venta,))
                items = cursor.fetchall()

                for item in items:
                    item["producto"] = Producto.get_by_id(item["id_producto"])
                    del item["id_producto"]
                    item["sabores"] = ItemVentaSabor.get_by_item_id(item["id"])
                return items

            except Exception as exc:
                print(f"Error en get_by_venta_id: {exc}")
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