from .precio_model import PrecioModel

class PrecioController:
    @staticmethod
    def get_all():
        precios = PrecioModel.get_all()
        return precios

    @staticmethod
    def get_one(id):
        precio = PrecioModel(id=id).get_by_id()
        return precio

    @staticmethod
    def create(data: dict) -> bool:
        precio = PrecioModel(
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"]
        )
        result = precio.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        precio = PrecioModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"]
        )
        result = precio.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        precio = PrecioModel(id=id)
        result = precio.delete(id)
        return result