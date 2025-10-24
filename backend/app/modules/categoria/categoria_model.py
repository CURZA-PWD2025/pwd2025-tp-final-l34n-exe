from ...database.conect_db import ConectDB

class CategoriaModel:
    def __init__(self, id:int=0, nombre:str="", tipo:str="", descripcion:str=""):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.descripcion = descripcion

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "descripcion": self.descripcion
        }

    @staticmethod
    def deserializar(data:dict) -> 'CategoriaModel':
        return CategoriaModel(
            id=data["id"],
            nombre=data["nombre"],
            tipo=data["tipo"],
            descripcion=data["descripcion"]
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM categoria")
                rows = cursor.fetchall()
                categorias=[]
                if rows:
                    for row in rows:
                        categorias.append(row)
                return categorias
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM categoria where id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    def create(self, data:dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO categoria (nombre, tipo, descripcion) VALUES (%s, %s, %s)", (self.nombre, self.tipo, self.descripcion))
                cnx.commit()
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
                cursor.execute("UPDATE categoria SET nombre=%s, tipo=%s, descripcion=%s WHERE id=%s", (self.nombre, self.tipo, self.descripcion, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar la categoria: {exc}"}
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM categoria WHERE id=%s", (self.id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al eliminar la categoria: {exc}"}
            finally:
                cnx.close()
