from ..database.conect_db import ConectDB
from ..precio.precio_model import PrecioModel as Precio

class ProductoModel:
    def __init__(self, id:int=0, descripcion:str="", precio:Precio = none, stock:int=0, fechaVcto:str=""):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.fechaVcto = fechaVcto

    def serializar(self)->dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio.serializar(),
            "stock": self.stock,
            "fechaVcto": self.fechaVcto
        }

    @staticmethod
    def deserializar(data:dict):
        return ProductoModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            fechaVcto=data["fechaVcto"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM producto")
                row = cursor.fetchall()
                productos=[]
                for row in rows:
                    productos.append(row)
                return productos
            except Exception as exc:
                print(f"Error:{exc}")

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM producto where id=%s", (self.id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error:{exc}")

    def create(self, data: dict) -> bool:
        cnx = ConectDB.getconnect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO producto (descripcion, precio, stock, fechaVcto) VALUES (%s)", (self.descripcion, self.precio, self.stock, self.fechaVcto))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el producto: {exc}"}
            finally:
                cnx.close()

    def update(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE producto SET descripcion = %s, precio = %s, stock = %s, fechaVcto = %s WHERE id = %s", (self.descripcion, self.precio, self.stock, self.fechaVcto, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el producto: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM producto WHERE id=%s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al borrar el producto: {exc}"}
            finally:
                cnx.close()


