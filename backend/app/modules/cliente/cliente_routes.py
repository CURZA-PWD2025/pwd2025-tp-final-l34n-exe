from .cliente_controller import ClienteController
from flask import jsonify, request, Blueprint

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route("/clientes", methods=['GET'])
def get_all():
    try:
        cliente = ClienteController.get_all()
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({"mensaje": "No se encontraron clientes"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route("/clientes/<int:id>", methods=['GET'])
def get_one(id):
    try:
        cliente = ClienteController.get_one(id)
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({"mensaje": "Cliente no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/clientes', methods=['POST'])
def create():
    try:
        data = request.get_json()
        cliente = ClienteController.create(data)
        if cliente:
            return jsonify({"mensaje": "Cliente creado exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/clientes/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        cliente = ClienteController.update(data)
        if cliente:
            return jsonify({"mensaje": "Cliente actualizado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        cliente = ClienteController.delete(id)
        if cliente:
            return jsonify({"mensaje": "Cliente eliminado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500