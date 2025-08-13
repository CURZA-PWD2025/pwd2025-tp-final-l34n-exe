from ..database.conect_db import ConectDB

class PrecioModel:
    #Constructor
    def __init__(self, id:int=0, precio:float=0.0):
        self.id = id
        self.precio = precio

    def serializar(self)->dict:
        return {
            "id": self.id,
            "precio": self.precio,
        }

    @staticmethod
    def deserializar(data:dict):
        return PrecioModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM precio")
                row = cursor.fetchall()
                precios=[]
                for row in rows:
                    precios.append(row)
                return precios
            except Exception as exc:
                print(f"Error:{exc}")

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM precio where id=%s", (self.id,))
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
                cursor.execute("INSERT INTO precio (precio) VALUES (%s)", (self.precio,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el precio: {exc}"}
            finally:
                cnx.close()

    def update(self, data: dict) -> bool:
        cnx = ConectDB.getconnect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE precio SET precio = %s WHERE id = %s", (self.precio, self.id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el precio: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.getconnect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM precio WHERE id=%s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al borrar el precio: {exc}"}
            finally:
                cnx.close()


