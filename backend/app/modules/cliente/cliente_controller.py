from .cliente_model import ClienteModel

class ClienteController:
    @staticmethod
    def get_all():
        clientes = ClienteModel.get_all()
        return clientes

    @staticmethod
    def get_one(id):
        cliente = ClienteModel(id=id).get_by_id()
        return cliente

    @staticmethod
    def create(data: dict) -> bool:
        cliente = ClienteModel(
            nombre=data["nombre"],
            apellido=data["apellido"],
            edad=data["edad"],
            direccion=data["direccion"]
        )
        result = cliente.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        cliente = ClienteModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            edad=data["edad"],
            direccion=data["direccion"]
        )
        result = cliente.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        cliente = ClienteModel(id=id)
        result = cliente.delete(id)
        return result