from .detalleventa_model import DetalleVentaModel

class DetalleVentaController:
    @staticmethod
    def get_all():
        detalles = DetalleVentaModel.get_all()
        return detalles

    @staticmethod
    def get_one(id):
        detalles = DetalleVentaModel(id=id).get_by_id()
        return detalles

    @staticmethod
    def create(data: dict) -> bool:
        detalles = DetalleVentaModel(
            nombre=data["nombre"]
        )
        result = detalles.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        detalles = DetalleVentaModel(
            id_venta=data["id_venta"],
            id_producto=data["id_producto"],
            cantidad=data["cantidad"],
            precio_unitario=data["precio_unitario"]
        )
        result = detalles.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        detalles = DetalleVentaModel(id=id)
        result = detalles.delete(id)
        return result