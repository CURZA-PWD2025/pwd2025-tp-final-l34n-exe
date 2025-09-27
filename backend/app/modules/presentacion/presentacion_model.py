from ..database.conect_db import ConectDB
from ..producto.producto_model import ProductoModel as Producto
from ..sabor.sabor_model import SaborModel as Sabor

class PresentacionModel:
    def __init__(self, id:int=0, producto:Producto=None, sabor:Sabor=None, stock:int=0):
        self.id = id
        self.producto = producto
        self.sabor = sabor
        self.stock = stock

    def serializar(self)->dict:
        return {
            "id": self.id,
            "producto": self.producto.serializar() if self.producto else None,
            "sabor": self.sabor.serializar() if self.sabor else None,
            "stock": self.stock
        }

    @staticmethod
    def deserializar(data:dict):
        return PresentacionModel(
            id=data["id"],
            producto=Producto.deserializar(data["producto"]) if data.get("producto") else None,
            sabor=Sabor.deserializar(data["sabor"]) if data.get("sabor") else None,
            stock=data["stock"]
        )

    @staticmethod
    def get_all()->list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM presentaciones")
                rows = cursor.fetchall()
                presentaciones=[]
                if rows:
                    for row in rows:
                        producto = Producto.get_by_id(row['id_producto'])
                        sabor = Sabor.get_by_id(row['id_sabor'])
                        row["producto"]=producto
                        row["sabor"]=sabor
                        presentaciones.append(row)
                return presentaciones
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM presentaciones where id=%s", (self.id,))
                row = cursor.fetchone()
                if row:
                    producto = Producto.get_by_id(row['id_producto'])
                    sabor = Sabor.get_by_id(row['id_sabor'])
                    row["producto"]=producto
                    row["sabor"]=sabor
                    return row
                return False
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    def create(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO presentaciones (id_producto, id_sabor, stock) VALUES (%s, %s, %s)", (self.id_producto, self.id_sabor, self.stock))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear: {exc}"}
            finally:
                cnx.close()

    def update(self, data:dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE presentaciones SET stock=%s WHERE id_producto=%s AND id_sabor=%s", (self.stock, self.producto.id, self.sabor.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM presentaciones WHERE id_producto=%s AND id_sabor=%s", (self.producto.id, self.sabor.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar: {exc}"}
            finally:
                cnx.close()


