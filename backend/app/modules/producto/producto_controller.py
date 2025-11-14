from .producto_model import ProductoModel
from app.modules.proveedor.proveedor_model import ProveedorModel
from app.modules.categoria.categoria_model import CategoriaModel

class ProductoController:
    @staticmethod
    def get_all() -> list[dict]:
        productos = ProductoModel.get_all()
        return productos

    @staticmethod
    def get_one(id) -> dict:
        producto = ProductoModel.get_by_id(id)
        return producto

    @staticmethod
    def create(data: dict) -> dict:
        proveedor_id = data["id_proveedor"]
        proveedor_data = ProveedorModel.get_by_id(proveedor_id)
        categoria_id = data["id_categoria"]
        categoria_data = CategoriaModel.get_by_id(categoria_id)

        if not proveedor_data:
            return {"mensaje": "El proveedor no existe"}
        if not categoria_data:
            return {"mensaje": "La categoría no existe"}

        proveedor = ProveedorModel.deserializar(proveedor_data)
        categoria = CategoriaModel.deserializar(categoria_data)

        producto = ProductoModel(
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            max_sabores=data["max_sabores"],
            proveedor=proveedor,
            categoria=categoria
        )
        result = producto.create()
        return {"resultado": result}


    @staticmethod
    def update(data: dict) -> dict:
        proveedor_id = data["id_proveedor"]
        proveedor_data = ProveedorModel.get_by_id(proveedor_id)
        categoria_id = data["id_categoria"]
        categoria_data = CategoriaModel.get_by_id(categoria_id)

        if not proveedor_data:
            return {"mensaje": "El proveedor no existe"}
        if not categoria_data:
            return {"mensaje": "La categoría no existe"}

        proveedor = ProveedorModel.deserializar(proveedor_data)
        categoria = CategoriaModel.deserializar(categoria_data)

        producto = ProductoModel(
            id=data["id"],
            nombre=data["nombre"],
            precio=data["precio"],
            stock=data["stock"],
            max_sabores=data["max_sabores"],
            proveedor=proveedor,
            categoria=categoria
        )
        result = producto.update()
        return {"resultado": result}

    @staticmethod
    def delete(id: int) -> dict:
        producto = ProductoModel(id=id)
        result = producto.delete()
        return {"resultado": result}