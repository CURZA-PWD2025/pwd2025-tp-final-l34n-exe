from .sabor_model import SaborModel
from ..categoria.categoria_model import CategoriaModel as Categoria

class SaborController:

    @staticmethod
    def get_all() -> list[dict]:
        return SaborModel.get_all()

    @staticmethod
    def get_one(id: int) -> dict:
        return SaborModel.get_by_id(id)

    @staticmethod
    def create(data: dict) -> dict:
        categoria_id = data["id_categoria"]
        categoria_data = Categoria.get_by_id(categoria_id)

        if not categoria_data:
            return {"mensaje": "La categoría no existe"}

        categoria = Categoria.deserializar(categoria_data)
        sabor = SaborModel(
            nombre=data["nombre"],
            stock=data["stock"],
            disponible=data["disponible"],
            categoria=categoria
        )
        return sabor.create()

    @staticmethod
    def update(data: dict) -> dict:
        categoria_id = data["id_categoria"]
        categoria_data = Categoria.get_by_id(categoria_id)

        if not categoria_data:
            return {"mensaje": "La categoría no existe"}

        categoria = Categoria.deserializar(categoria_data)
        sabor = SaborModel(
            id=data["id"],
            nombre=data["nombre"],
            stock=data["stock"],
            disponible=data["disponible"],
            categoria=categoria
        )
        return sabor.update()

    @staticmethod
    def delete(id: int) -> dict:
        sabor = SaborModel(id=id)
        return sabor.delete()
