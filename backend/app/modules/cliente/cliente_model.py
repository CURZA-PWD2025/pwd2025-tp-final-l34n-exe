from ...database.conect_db import ConectDB

class ClienteModel:
    def __init__(self, id:int=0, nombre:str="", apellido:str="", telefono:str="", direccion:str=""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion


    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "direccion": self.direccion
        }

    @staticmethod
    def deserializar(data:dict) -> 'ClienteModel':
        return ClienteModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            direccion=data["direccion"]
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM clientes")
                rows = cursor.fetchall()
                clientes=[]
                if rows:
                    for row in rows:
                        clientes.append(row)
                return clientes
            except Exception as exc:
                print(f"Error:{exc}")
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM clientes where id=%s", (id,))
                row = cursor.fetchone()
                if row:
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
                cursor.execute("INSERT INTO clientes (nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s)", (self.nombre, self.apellido, self.telefono, self.direccion))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el cliente: {exc}"}
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE clientes SET nombre=%s, apellido=%s, telefono=%s, direccion=%s WHERE id=%s", (self.nombre, self.apellido, self.telefono, self.direccion, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el cliente: {exc}"}
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM clientes WHERE id=%s", (self.id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al eliminar el cliente: {exc}"}
            finally:
                cnx.close()


