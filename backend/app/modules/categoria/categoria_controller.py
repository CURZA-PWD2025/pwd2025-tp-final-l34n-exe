from .categoria_model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        categorias = CategoriaModel.get_all()
        return categorias

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel(id=id).get_by_id()
        return categoria

    @staticmethod
    def create(data: dict) -> bool:
        categoria = CategoriaModel(
            nombre=data["nombre"]
        )
        result = categoria.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        categoria = CategoriaModel(
            id=data["id"],
            nombre=data["nombre"]
        )
        result = categoria.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        categoria = CategoriaModel(id=id)
        result = categoria.delete(id)
        return result


