from ...database.conect_db import ConectDB

class EmpleadoModel:
    def __init__(self, id:int=0, nombre:str="", apellido:str="", telefono:str="", email:str="", puesto:str=""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.puesto = puesto

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email,
            "puesto": self.puesto
        }

    @staticmethod
    def deserializar(data:dict) -> 'EmpleadoModel':
        return EmpleadoModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            email=data["email"],
            puesto=data["puesto"]
        )

    @staticmethod
    def get_all() -> list[dict]:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM empleados")
                rows = cursor.fetchall()
                empleados=[]
                if rows:
                    for row in rows:
                        empleados.append(row)
                return empleados
            except Exception as exc:
                return {"mensaje": f"Error al obtener los empleados: {exc}"}
            finally:
                cnx.close()

    @staticmethod
    def get_by_id(id:int) -> dict:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM empleados where id=%s", (id,))
                row = cursor.fetchone()
                if row:
                    return row
                return None
            except Exception as exc:
                return {"mensaje": f"Error al obtener el cliente: {exc}"}
            finally:
                cnx.close()

    def create(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO empleados (nombre, apellido, telefono, email, puesto) VALUES (%s, %s, %s, %s, %s)", (self.nombre, self.apellido, self.telefono, self.email, self.puesto))
                self.id = cursor.lastrowid
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al crear el empleado: {exc}"})
                return False
            finally:
                cnx.close()

    def update(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("UPDATE empleados SET nombre=%s, apellido=%s, telefono=%s, email=%s, puesto=%s WHERE id=%s", (self.nombre, self.apellido, self.telefono, self.email, self.puesto, self.id))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al actualizar el empleado: {exc}"})
                return False
            finally:
                cnx.close()

    def delete(self) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM empleados WHERE id=%s", (self.id,))
                cnx.commit()
                return cursor.rowcount > 0
            except Exception as exc:
                cnx.rollback()
                print({"mensaje": f"Error al eliminar el empleado: {exc}"})
                return False
            finally:
                cnx.close()