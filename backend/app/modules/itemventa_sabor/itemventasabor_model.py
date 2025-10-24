from ...database.conect_db import ConectDB
from ..sabor.sabor_model import SaborModel as Sabor
from ..item_venta.itemventa_model import ItemVentaModel as ItemVenta

class ItemVentaSaborModel:
    def __init__(self, id:int=0, item_venta:ItemVenta=None, sabor:Sabor=None):
        self.id = id
        self.item_venta = item_venta
        self.sabor = sabor

    def serializar(self)->dict:
        return {
            "id": self.id,
            "item_venta": self.item_venta.serializar() if self.item_venta else None,
            "sabor": self.sabor.serializar() if self.sabor else None
        }

    @staticmethod
    def deserializar(data:dict) -> 'ItemVentaSaborModel':
        return ItemVentaSaborModel(
            id=data["id"],
            item_venta=ItemVenta.deserializar(data["item_venta"]) if data["item_venta"] else None,
            sabor=Sabor.deserializar(data["sabor"]) if data["sabor"] else None
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_venta_sabores")
                rows = cursor.fetchall()
                items_venta_sabores = []
                for row in rows:
                    items_venta_sabores.append(row)
                return items_venta_sabores
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM items_venta_sabores where id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_item_id(id_item_venta: int) -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT s.id, s.nombre FROM items_venta_sabores ivs JOIN sabores s ON ivs.id_sabor = s.id WHERE ivs.id_item = %s", (id_item_venta,))
                return cursor.fetchall()
            except Exception as exc:
                print(f"Error: {exc}")
                return []
            finally:
                cnx.close()


    def create(self) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                sql = "INSERT INTO items_venta_sabores (id_item, id_sabor) VALUES (%s, %s)"
                values = (self.item_venta.id, self.sabor.id)
                cursor.execute(sql, values)
                cnx.commit()
                return {"mensaje": "ItemVentaSabor creado exitosamente", "id": cursor.lastrowid}
            except Exception as exc:
                print(f"Error: {exc}")
                return {"mensaje": "Error al crear ItemVentaSabor"}
            finally:
                cnx.close()

    def update(self) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                sql = "UPDATE items_venta_sabores SET id_item=%s, id_sabor=%s WHERE id=%s"
                values = (self.item_venta.id, self.sabor.id, self.id)
                cursor.execute(sql, values)
                cnx.commit()
                return {"mensaje": "ItemVentaSabor actualizado exitosamente"}
            except Exception as exc:
                print(f"Error:{exc}")
                return {"mensaje": "Error al actualizar ItemVentaSabor"}
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM items_venta_sabores WHERE id=%s", (self.id,))
                cnx.commit()
                return True
            except Exception as exc:
                print(f"Error:{exc}")
                return False
            finally:
                cnx.close()