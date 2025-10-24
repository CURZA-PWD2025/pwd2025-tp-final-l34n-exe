from .itemventa_controller import ItemVentaController
from flask import jsonify, request, Blueprint

itemventa_bp = Blueprint('itemventa', __name__)

@itemventa_bp.route("/itemventa", methods=['GET'])
def get_all():
    try:
        items = ItemVentaController.get_all()
        if items:
            return jsonify(items), 200
        else:
            return jsonify({"mensaje": "No se encontraron items"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventa_bp.route("/itemventa/<int:id>", methods=['GET'])
def get_one(id:int):
    try:
        item = ItemVentaController.get_one(id)
        if item:
            return jsonify(item), 200
        else:
            return jsonify({"mensaje": "Item no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventa_bp.route('/itemventa', methods=['POST'])
def create():
    try:
        data = request.get_json()
        result = ItemVentaController.create(data)
        if result:
            return jsonify({"mensaje": "Item de venta creado exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear el item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventa_bp.route('/itemventa/<int:id>', methods=['PUT'])
def update(id:int):
    try:
        data = request.get_json()
        data["id"] = id
        result = ItemVentaController.update(data)
        if result:
            return jsonify({"mensaje": "Item de venta actualizado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar el item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@itemventa_bp.route('/itemventa/<int:id>', methods=['DELETE'])
def delete(id:int):
    try:
        result = ItemVentaController.delete(id)
        if result:
            return jsonify({"mensaje": "Item de venta eliminado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar el item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500
