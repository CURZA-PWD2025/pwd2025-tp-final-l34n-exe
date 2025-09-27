from .cliente_controller import DetalleVentaController
from flask import jsonify, request, Blueprint

detalleventa_bp = Blueprint('detalleventa', __name__)

@detalleventa_bp.route("/detalleventa", methods=['GET'])
def get_all():
    try:
        detalles = DetalleVentaController.get_all()
        if detalles:
            return jsonify(detalles), 200
        else:
            return jsonify({"mensaje": "No se encontraron detalles"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route("/detalleventa/<int:id>", methods=['GET'])
def get_one(id):
    try:
        cliente = DetalleVentaController.get_one(id)
        if cliente:
            return jsonify(cliente), 200
        else:
            return jsonify({"mensaje": "Cliente no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/detalleventa', methods=['POST'])
def create():
    try:
        data = request.get_json()
        cliente = DetalleVentaController.create(data)
        if cliente:
            return jsonify({"mensaje": "Cliente creado exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/detalleventa/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        cliente = DetalleVentaController.update(data)
        if cliente:
            return jsonify({"mensaje": "Cliente actualizado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@cliente_bp.route('/detalleventa/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        cliente = DetalleVentaController.delete(id)
        if cliente:
            return jsonify({"mensaje": "Cliente eliminado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar el cliente"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500