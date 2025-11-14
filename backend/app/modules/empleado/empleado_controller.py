from .empleado_model import EmpleadoModel

class EmpleadoController:
    @staticmethod
    def get_all() -> list[dict]:
        empleado = EmpleadoModel.get_all()
        return empleado

    @staticmethod
    def get_one(id) -> dict:
        empleado = EmpleadoModel.get_by_id(id)
        return empleado

    @staticmethod
    def create(data: dict) -> dict:
        empleado = EmpleadoModel(
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data.get("telefono"),
            email=data.get("email"),
            puesto=data["puesto"]
        )
        result = empleado.create()
        return {"Creado": result}

    @staticmethod
    def update(data: dict) -> dict:
        empleado = EmpleadoModel(
            id= data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            telefono=data.get("telefono"),
            email=data.get("email"),
            puesto=data["puesto"]
        )
        result = empleado.update()
        return {"Actualizado": result}

    @staticmethod
    def delete(id: int) -> dict:
        empleado = EmpleadoModel(id=id)
        result = empleado.delete()
        return {"Eliminado": result}