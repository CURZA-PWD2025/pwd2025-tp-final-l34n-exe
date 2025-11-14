from ...database.conect_db import ConectDB

class ProveedorModel:
    def __init__(self, id:int=0, nombre:str="", telefono:str="", email:str=""):
        self.id = id
        self.nombre= nombre
        self.telefono =telefono
        self.email = email

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

    @staticmethod
    def deserializar(data:dict) -> 'ProveedorModel':
        return ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            email=data["email"]
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM proveedores")
                rows = cursor.fetchall()
                proveedores = []
                if rows:
                    for row in rows:
                        proveedores.append(row)
                return proveedores
            except Exception as exc:
                return {"error": f"Error al obtener los proveedores: {exc}"}

            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM proveedores WHERE id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    return row
                return None
            except Exception as exc:
                return {"error": f"Error al obtener los proveedores: {exc}"}
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "INSERT INTO proveedores (nombre, telefono, email) VALUES (%s, %s, %s)",
                    (self.nombre, self.telefono, self.email)
                )
                self.id = cursor.lastrowid
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al crear el proveedor: {exc}"})
                return False
            finally:
                cnx.close()


    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute(
                    "DELETE FROM proveedores WHERE id = %s",
                    (self.id,)
                )
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al eliminar el proveedor: {exc}"})
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE proveedores SET nombre=%s, telefono=%s, email=%s WHERE id=%s", (self.nombre, self.telefono, self.email, self.id))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al actualizar el proveedor: {exc}"})
                return False
            finally:
                cnx.close()
