from .sabor_controller import SaborController
from flask import jsonify, request, Blueprint

sabor_bp = Blueprint('sabor', __name__)

@sabor_bp.route("/sabores", methods=['GET'])
def get_all():
    try:
        sabores = SaborController.get_all()
        if sabores:
            return jsonify(sabores), 200
        else:
            return jsonify({"mensaje": "No se encontraron sabores"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@sabor_bp.route("/sabores/<int:id>", methods=['GET'])
def get_one(id:int):
    try:
        sabor = SaborController.get_one(id)
        if sabor:
            return jsonify(sabor), 200
        else:
            return jsonify({"mensaje": "Sabor no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@sabor_bp.route('/sabores', methods=['POST'])
def create():
    try:
        data = request.get_json()
        sabor = SaborController.create(data)
        if sabor:
            return jsonify({"message": "Sabor creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear el sabor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@sabor_bp.route('/sabores/<int:id>', methods=['PUT'])
def update(id:int):
    try:
        data = request.get_json()
        data['id'] = id
        sabor = SaborController.update(data)
        if sabor:
            return jsonify({"message": "Sabor actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el sabor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@sabor_bp.route('/sabores/<int:id>', methods=['DELETE'])
def delete(id:int):
    try:
        sabor = SaborController.delete(id)
        if sabor:
            return jsonify({"message": "Sabor eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar el sabor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500
