from ..database.conect_db import ConectDB

class SaborModel:

    def __init__(self, id:int=0, nombre:str=""):
        self.id = id
        self.nombre = nombre

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    @staticmethod
    def deserializar(data:dict):
        return SaborModel(
            id=data["id"],
            nombre=data["nombre"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM sabores")
                rows = cursor.fetchall()
                sabores=[]
                for row in rows:
                    sabores.append(row)
                return sabores
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM sabores where id=%s", (self.id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error:{exc}")

    def create(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO sabores (nombre) VALUES (%s)", (self.nombre))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el sabor: {exc}"}
            finally:
                cnx.close()

    def update(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE sabores SET nombre = %s WHERE id = %s", (self.nombre, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar los sabores: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM sabores WHERE id=%s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al borrar el sabor: {exc}"}
            finally:
                cnx.close()


