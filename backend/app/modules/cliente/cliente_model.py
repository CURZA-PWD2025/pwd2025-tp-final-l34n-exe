from ..database.conect_db import ConectDB

class ClienteModel:
    def __init__(self, id:int=0, nombre:str="", apellido:str="", edad:int=0, direccion:str=""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "direccion": self.direccion
        }

    @staticmethod
    def deserializar(data:dict):
        return ClienteModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            edad=data["edad"],
            direccion=data["direccion"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM clientes")
                row = cursor.fetchall()
                clientes=[]
                for row in rows:
                    clientes.append(row)
                return clientes
            except Exception as exc:
                print(f"Error:{exc}")
                
    @staticmethod
    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM clientes where id=%s", (self.id,))
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
                cursor.execute("INSERT INTO clientes (nombre, apellido, edad, direccion) VALUES (%s)", (self.nombre, self.apellido, self.edad, self.direccion))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el Cliente: {exc}"}
            finally:
                cnx.close()

    def update(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE clientes SET nombre = %s, apellido = %s, edad = %s, direccion = %s WHERE id = %s", (self.nombre, self.apellido, self.edad, self.direccion, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el Cliente: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al borrar el clientes: {exc}"}
            finally:
                cnx.close()


