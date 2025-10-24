from .categoria_model import CategoriaModel

class CategoriaController:

    @staticmethod
    def get_all() -> list[dict]:
        categoria = CategoriaModel.get_all()
        return categoria

    @staticmethod
    def get_one(id) -> dict:
        categoria = CategoriaModel().get_by_id(id)
        return categoria

    @staticmethod
    def create(data: dict) -> dict:
        categoria = CategoriaModel(
            nombre=data["nombre"],
            tipo=data["tipo"],
            descripcion=data["descripcion"]
        )
        result = categoria.create(data)
        return result

    @staticmethod
    def update(data: dict) -> dict:
        categoria = CategoriaModel(
            id= data["id"],
            nombre=data["nombre"],
            tipo=data["tipo"],
            descripcion=data["descripcion"]
        )
        result = categoria.update()
        return result

    @staticmethod
    def delete(id: int) -> dict:
        categoria = CategoriaModel(id=id)
        result = categoria.delete()
        return result