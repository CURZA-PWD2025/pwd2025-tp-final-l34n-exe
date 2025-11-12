from ...database.conect_db import ConectDB
from ..categoria.categoria_model import CategoriaModel as Categoria

class SaborModel:

    def __init__(self, id:int=0, nombre:str="", stock:float=0.0, disponible:bool=True, categoria:Categoria=None):
        self.id = id
        self.nombre = nombre
        self.stock = stock
        self.disponible = disponible
        self.categoria = categoria


    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "stock": self.stock,
            "disponible": self.disponible,
            "categoria": self.categoria.serializar() if self.categoria else None
        }

    @staticmethod
    def deserializar(data:dict) -> 'SaborModel':
        return SaborModel(
            id=data["id"],
            nombre=data["nombre"],
            stock=data["stock"],
            disponible=data["disponible"],
            categoria=Categoria.deserializar(data["categoria"]) if data.get("categoria") else None
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM sabores")
                rows = cursor.fetchall()
                sabores = []
                if rows:
                    for row in rows:
                        categoria = Categoria.get_by_id(row["id_categoria"])
                        del row["id_categoria"]
                        row["categoria"] = categoria
                        sabores.append(row)
                return sabores
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
                cursor.execute("SELECT * FROM sabores where id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    row["categoria"] = Categoria.get_by_id(row["id_categoria"])
                    del row["id_categoria"]
                return row
            except Exception as exc:
                return (f"Error:{exc}")
            finally:
                cnx.close()


    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True)  as cursor:
            try:
                cursor.execute("INSERT INTO sabores (nombre, stock, disponible, id_categoria) VALUES (%s, %s, %s, %s)", (self.nombre, self.stock, self.disponible, self.categoria.id))
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

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE sabores SET nombre = %s, stock = %s, disponible = %s, id_categoria = %s WHERE id = %s", (self.nombre, self.stock, self.disponible, self.categoria.id, self.id))
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

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM sabores WHERE id=%s", (self.id,))
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


