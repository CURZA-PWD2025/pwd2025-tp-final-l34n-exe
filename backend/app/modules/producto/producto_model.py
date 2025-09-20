from ..database.conect_db import ConectDB

class ProductoModel:
    def __init__(self, id:int=0, tipo:str="", precio:float=0.0, stock:int=0, fechaVcto:str=""):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.stock = stock
        self.fechaVcto = fechaVcto

    def serializar(self)->dict:
        return {
            "id": self.id,
            "tipo": self.tipo,
            "precio": self.precio,
            "stock": self.stock,
            "fechaVcto": self.fechaVcto
        }

    @staticmethod
    def deserializar(data:dict):
        return ProductoModel(
            id=data["id"],
            tipo=data["tipo"],
            precio=data["precio"],
            stock=data["stock"],
            fechaVcto=data["fechaVcto"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM productos")
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
                cursor.execute("SELECT * FROM productos where id=%s", (self.id,))
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
                cursor.execute("INSERT INTO productos (tipo, precio, stock, fechaVcto) VALUES (%s)", (self.tipo, self.precio, self.stock, self.fechaVcto))
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
                cursor.execute("UPDATE productos SET tipo = %s, precio = %s, stock = %s, fechaVcto = %s WHERE id = %s", (self.tipo, self.precio, self.stock, self.fechaVcto, self.id))
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
                cursor.execute("DELETE FROM productos WHERE id=%s", (id,))
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


