from .empleado_controller import EmpleadoController
from flask import jsonify, request, Blueprint

empleado_bp = Blueprint('empleado', __name__)
@empleado_bp.route("/empleado", methods=['GET'])
def get_all():
    try:
        empleado = EmpleadoController.get_all()
        if empleado:
            return jsonify(empleado), 200
        else:
            return jsonify({"mensaje": "No se encontraron empleados"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@empleado_bp.route("/empleado/<int:id>", methods=['GET'])
def get_one(id):
    try:
        empleado = EmpleadoController.get_one(id)
        if empleado:
            return jsonify(empleado), 200
        else:
            return jsonify({"mensaje": "Empleado no encontrada"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@empleado_bp.route('/empleado', methods=['POST'])
def create():
    try:
        data = request.get_json()
        empleado = EmpleadoController.create(data)
        if empleado:
            return jsonify({"message": "Empleado creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear el empleado"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@empleado_bp.route('/empleado/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        empleado = EmpleadoController.update(data)
        if empleado:
            return jsonify({"message": "Empleado actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el empleado"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@empleado_bp.route('/empleado/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        empleado = EmpleadoController.delete(id)
        if empleado:
            return jsonify({"message": "Empleado eliminada exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar el empleado"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500