from .sabor_model import SaborModel

class SaborController:
    @staticmethod
    def get_all():
        sabores = SaborModel.get_all()
        return sabores

    @staticmethod
    def get_one(id):
        sabor = SaborModel(id=id).get_by_id()
        return sabor

    @staticmethod
    def create(data: dict) -> bool:
        sabor = SaborModel(
            nombre=data["nombre"],
        )
        result = sabor.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        sabor = SaborModel(
            id=data["id"],
            nombre=data["nombre"],
        )
        result = sabor.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        sabor = SaborModel(id=id)
        result = sabor.delete(id)
        return result