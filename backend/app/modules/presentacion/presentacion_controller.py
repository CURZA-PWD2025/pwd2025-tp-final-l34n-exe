from .presentacion_model import PresentacionModel

class PresentacionController:
    @staticmethod
    def get_all():
        presentacion = PresentacionModel.get_all()
        return presentacion

    @staticmethod
    def get_one(id):
        presentacion = PresentacionModel(id=id).get_by_id()
        return presentacion

    @staticmethod
    def create(data: dict) -> bool:
        presentacion = PresentacionModel(
            producto=data["id_producto"],
            sabor=data["id_sabor"],
            stock=data["stock"]
        )
        result = presentacion.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        presentacion = PresentacionModel(
            id= data["id"],
            producto=data["id_producto"],
            sabor=data["id_sabor"],
            stock=data["stock"]
        )
        result = presentacion.update()
        return result

    @staticmethod
    def delete(id: int) -> bool:
        presentacion = PresentacionModel(id=id)
        result = presentacion.delete()
        return result