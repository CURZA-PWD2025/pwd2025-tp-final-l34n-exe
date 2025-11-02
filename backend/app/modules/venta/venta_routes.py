from .venta_controller import VentaController
from flask import jsonify, request, Blueprint

venta_bp = Blueprint('venta', __name__)

@venta_bp.route("/ventas", methods=['GET'])
def get_all():
    try:
        ventas = VentaController.get_all()
        if ventas:
            return jsonify(ventas), 200
        else:
            return jsonify({"mensaje": "No se encontraron ventas"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@venta_bp.route("/ventas/<int:id>", methods=['GET'])
def get_one(id: int):
    try:
        venta = VentaController.get_one(id)
        if venta:
            return jsonify(venta), 200
        else:
            return jsonify({"mensaje": "Venta no encontrada"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@venta_bp.route('/ventas', methods=['POST'])
def create():
    try:
        data = request.get_json()
        venta = VentaController.create(data)
        if venta:
            return jsonify({"mensaje": "Venta creada exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear la venta"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@venta_bp.route('/ventas/<int:id>', methods=['PUT'])
def update(id: int):
    try:
        data = request.get_json()
        data['id'] = id
        venta = VentaController.update(data)
        if venta:
            return jsonify({"mensaje": "Venta actualizada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar la venta"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@venta_bp.route('/ventas/<int:id>', methods=['DELETE'])
def delete(id: int):
    try:
        venta = VentaController.delete(id)
        if venta:
            return jsonify({"mensaje": "Venta eliminada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar la venta"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500