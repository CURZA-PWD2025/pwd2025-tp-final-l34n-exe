from ..database.conect_db import ConectDB

class EmpleadoModel:
    def __init__(self, id:int=0, nombre:str="", apellido:str="", puesto:str="", salario:float=0.0):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto
        self.salario = salario

    def serializar(self)->dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "puesto": self.puesto,
            "salario": self.salario
        }

    @staticmethod
    def deserializar(data:dict):
        return EmpleadoModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            puesto=data["puesto"],
            salario=data["salario"]
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM empleados")
                row = cursor.fetchall()
                empleados=[]
                for row in rows:
                    empleados.append(row)
                return empleados
            except Exception as exc:
                print(f"Error:{exc}")

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM empleados where id=%s", (self.id,))
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
                cursor.execute("INSERT INTO empleados (nombre, apellido, puesto, salario) VALUES (%s)", (self.nombre, self.apellido, self.puesto, self.salario))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear el empleado: {exc}"}
            finally:
                cnx.close()

    def update(self, data: dict) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("UPDATE empleados SET nombre = %s, apellido = %s, puesto = %s, salario = %s WHERE id = %s", (self.nombre, self.apellido, self.puesto, self.salario, self.id))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al actualizar el empleado: {exc}"}
            finally:
                cnx.close()

    def delete(self, id: int) -> bool:
        cnx = ConectDB.get_connect()
        with cnx.cursor() as cursor:
            try:
                cursor.execute("DELETE FROM empleados WHERE id=%s", (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al borrar el empleado: {exc}"}
            finally:
                cnx.close()


