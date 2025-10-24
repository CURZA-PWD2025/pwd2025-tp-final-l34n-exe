from .cliente_model import ClienteModel

class ClienteController:

    @staticmethod
    def get_all() -> list[dict]:
        cliente = ClienteModel.get_all()
        return cliente

    @staticmethod
    def get_one(id) -> dict:
        cliente = ClienteModel().get_by_id(id)
        return cliente

    @staticmethod
    def create(data: dict) -> dict:
        cliente = ClienteModel(
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            direccion=data["direccion"]
        )
        result = cliente.create(data)
        return result

    @staticmethod
    def update(data: dict) -> dict:
        cliente = ClienteModel(
            id= data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data["telefono"],
            direccion=data["direccion"]
        )
        result = cliente.update()
        return result

    @staticmethod
    def delete(id: int) -> dict:
        cliente = ClienteModel(id=id)
        result = cliente.delete()
        return result