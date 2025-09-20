from .venta_model import VentaModel

class VentaController:
    @staticmethod
    def get_all():
        ventas = VentaModel.get_all()
        return ventas

    @staticmethod
    def get_one(id):
        venta = VentaModel(id=id).get_by_id()
        return venta

    @staticmethod
    def create(data: dict) -> bool:
        venta = VentaModel(
            total=data["total"],
            fecha=data["fecha"],
            id_producto=data["id_producto"],
            id_cliente=data["id_cliente"],
            id_empleado=data["id_empleado"],
        )
        result = venta.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        venta = VentaModel(
            id=data["id"],
            total=data["total"],
            fecha=data["fecha"],
            id_producto=data["id_producto"],
            id_cliente=data["id_cliente"],
            id_empleado=data["id_empleado"],
        )
        result = venta.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        venta = VentaModel(id=id)
        result = venta.delete(id)
        return result