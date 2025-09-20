from .empleado_model import EmpleadoModel

class empleadoController:
    @staticmethod
    def get_all():
        empleados = EmpleadoModel.get_all()
        return empleados

    @staticmethod
    def get_one(id):
        empleado = EmpleadoModel(id=id).get_by_id()
        return empleado

    @staticmethod
    def create(data: dict) -> bool:
        empleado = EmpleadoModel(
            nombre=data["nombre"],
            apellido=data["apellido"],
            puesto=data["puesto"],
            salario=data["salario"]
        )
        result = empleado.create(data)
        return result

    @staticmethod
    def update(data: dict) -> bool:
        empleado = EmpleadoModel(
            id=data["id"],
            nombre=data["nombre"],
            apellido=data["apellido"],
            puesto=data["puesto"],
            salario=data["salario"]
        )
        result = empleado.update(data)
        return result

    @staticmethod
    def delete(id: int) -> bool:
        empleado = EmpleadoModel(id=id)
        result = empleado.delete(id)
        return result