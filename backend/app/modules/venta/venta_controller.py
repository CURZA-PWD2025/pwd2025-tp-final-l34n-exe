from .venta_model import VentaModel
from app.modules.cliente.cliente_model import ClienteModel
from app.modules.empleado.empleado_model import EmpleadoModel
class VentaController:

    @staticmethod
    def get_all() -> list[dict]:
        ventas = VentaModel.get_all()
        return ventas

    @staticmethod
    def get_one(id) -> dict:
        venta = VentaModel.get_by_id(id)
        return venta

    @staticmethod
    def create(data: dict) -> dict:
        cliente_id = data["id_cliente"]
        empleado_id = data["id_empleado"]

        cliente_data = ClienteModel.get_by_id(cliente_id)
        empleado_data = EmpleadoModel.get_by_id(empleado_id)

        if not cliente_data:
            return {"mensaje": "El cliente no existe"}

        if not empleado_data:
            return {"mensaje": "El empleado no existe"}

        cliente = ClienteModel.deserializar(cliente_data)
        empleado = EmpleadoModel.deserializar(empleado_data)

        venta = VentaModel(
            fecha=data["fecha"],
            total=data["total"],
            cliente=cliente,
            empleado=empleado
        )
        result = venta.create()
        return result


    @staticmethod
    def update(data: dict) -> dict:
        cliente_id = data["id_cliente"]
        empleado_id = data["id_empleado"]

        cliente_data = ClienteModel.get_by_id(cliente_id)
        empleado_data = EmpleadoModel.get_by_id(empleado_id)

        if not cliente_data:
            return {"mensaje": "El cliente no existe"}
        
        if not empleado_data:
            return {"mensaje": "El empleado no existe"}

        cliente = ClienteModel.deserializar(cliente_data)
        empleado = EmpleadoModel.deserializar(empleado_data)

        venta = VentaModel(
            id=data["id"],
            fecha=data["fecha"],
            total=data["total"],
            cliente=cliente,
            empleado=empleado
        )
        result = venta.update()
        return result


    @staticmethod
    def delete(id: int) -> dict:
        venta = VentaModel(id=id)
        result = venta.delete()
        return result