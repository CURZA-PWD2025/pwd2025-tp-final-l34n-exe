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
                if rows:
                    for row in rows:
                        row["itemventa"] = ItemVenta.get_by_id(row["id_item"])
                        del row["id_item"]
                        row["sabor"] = Sabor.get_by_id(row["id_sabor"])
                        del row["id_sabor"]
                        items_venta_sabores.append(row)
                    return items_venta_sabores
            except Exception as exc:
                return {"mensaje": f"Error al obtener los items_venta_sabores: {exc}"}
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id: int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
              cursor.execute("SELECT * FROM items_venta_sabores WHERE id = %s", (id,))
              row = cursor.fetchone()
              if row:
                  row["itemventa"] = ItemVenta.get_by_id(row["id_item"])
                  del row["id_item"]
                  row["sabor"] = Sabor.get_by_id(row["id_sabor"])
                  del row["id_sabor"]
              return row
            except Exception as exc:
              return {"mensaje": f"Error al obtener el item_venta_sabor: {exc}"}
            finally:
              cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO items_venta_sabores (id_item, id_sabor) VALUES (%s, %s)",
                    (self.item_venta.id if self.item_venta else None,
                     self.sabor.id if self.sabor else None)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al crear el item-venta_sabor:{exc}"})
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute(
                    "UPDATE items_venta_sabores SET id_item=%s, id_sabor=%s WHERE id=%s",
                    (self.item_venta.id if self.item_venta else None,
                     self.sabor.id if self.sabor else None,
                     self.id)
                )
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al actualizar el item-venta_sabor:{exc}"})
                return False
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
                cnx.rollback()
                print({"mensaje": f"Error al eliminar el item-venta_sabor:{exc}"})
                return False
            finally:
                cnx.close()