from .itemventasabor_controller import ItemVentaSaborController
from flask import jsonify, request, Blueprint

itemventasabor_bp = Blueprint('itemventasabor', __name__)

@itemventasabor_bp.route("/itemventasabores", methods=['GET'])
def get_all():
    try:
        items = ItemVentaSaborController.get_all()
        if items:
            return jsonify(items), 200
        else:
            return jsonify({"mensaje": "No se encontraron items"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventasabor_bp.route("/itemventasabores/<int:id>", methods=['GET'])
def get_one(id:int):
    try:
        item = ItemVentaSaborController.get_one(id)
        if item:
            return jsonify(item), 200
        else:
            return jsonify({"mensaje": "Item no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventasabor_bp.route('/itemventasabores', methods=['POST'])
def create():
    try:
        data = request.get_json()
        result = ItemVentaSaborController.create(data)
        if result:
            return jsonify({"mensaje": "Sabores de los items creados exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear el sabor del item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@itemventasabor_bp.route('/itemventasabores/<int:id>', methods=['PUT'])
def update(id:int):
    try:
        data = request.get_json()
        data["id"] = id
        result = ItemVentaSaborController.update(data)
        if result:
            return jsonify({"mensaje": "Sabor del item actualizados exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar sabor del item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@itemventasabor_bp.route('/itemventasabores/<int:id>', methods=['DELETE'])
def delete(id:int):
    try:
        result = ItemVentaSaborController.delete(id)
        if result:
            return jsonify({"mensaje": "Sabores de los items eliminado exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar el sabor del item"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


