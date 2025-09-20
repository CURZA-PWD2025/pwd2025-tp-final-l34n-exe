from ..database.conect_db import ConectDB

class VentaModel:
    def __init__(self, id:int=0, total:float=0.0, fecha:str="", id_producto:int=0, id_cliente:int=0, id_empleado:int=0):
        self.id = id
        self.total = total
        self.fecha = fecha
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.id_empleado = id_empleado

    def serializar(self)->dict:
        return {
            "id": self.id,
            "total": self.total,
            "fecha": self.fecha,
            "id_producto": self.id_producto,
            "id_cliente": self.id_cliente,
            "id_empleado": self.id_empleado,
        }

    @staticmethod
    def deserializar(data:dict):
        return VentaModel(
            id=data["id"],
            total=data["total"],
            fecha=data["fecha"],
            id_producto=data["id_producto"],
            id_cliente=data["id_cliente"],
            id_empleado=data["id_empleado"],
        )

    @staticmethod
    def get_all():
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM venta")
                rows = cursor.fetchall()
                ventas=[]
                for row in rows:
                    ventas.append(row)
                return ventas
            except Exception as exc:
                print(f"Error:{exc}")

    def get_by_id(self):
        cnx = ConectDB.get_connect()
        with cnx.cursor(dictionary=True) as cursor:
            try:
                cursor.execute("SELECT * FROM venta where id=%s", (self.id,))
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
                cursor.execute("INSERT INTO venta (total, fecha, id_producto, id_cliente, id_empleado) VALUES (%s, %s, %s, %s, %s)",
                               (self.total, self.fecha, self.id_producto, self.id_cliente, self.id_empleado))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {"mensaje": f"Error al crear la venta: {exc}"}