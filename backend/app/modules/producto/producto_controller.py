from .producto_model import ProductoModel

class ProductoController:
    @staticmethod
    def get_all():
        productos = ProductoModel.get_all()
        return productos

    @staticmethod
    def get_one(id):
        producto = ProductoModel(id=id).get_by_id()
        return producto

    @staticmethod
    def create(data: dict) -> bool:
        producto = ProductoModel(
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            fechaVcto=data["fechaVcto"]
        )
        result = producto.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        producto = ProductoModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            fechaVcto=data["fechaVcto"]
        )
        result = producto.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        producto = ProductoModel(id=id)
        result = producto.delete(id)
        return result