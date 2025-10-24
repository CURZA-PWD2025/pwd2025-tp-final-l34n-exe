from .proveedor_model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all() -> list[dict]:
        proveedores = ProveedorModel.get_all()
        return proveedores

    @staticmethod
    def get_one(id) -> dict:
        proveedores = ProveedorModel.get_by_id(id)
        return proveedores

    @staticmethod
    def create(data: dict) -> dict:
        proveedores = ProveedorModel(
            nombre=data["nombre"],
            telefono=data["telefono"],
            email=data["email"]
        )
        result = proveedores.create()
        return result

    @staticmethod
    def update(data: dict) -> dict:
        proveedores = ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            email=data["email"]
        )
        result = proveedores.update()
        return result

    @staticmethod
    def delete(id: int) -> dict:
        proveedores = ProveedorModel(id=id)
        result = proveedores.delete()
        return result