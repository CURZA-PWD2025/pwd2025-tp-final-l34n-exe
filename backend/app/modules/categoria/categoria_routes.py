from .categoria_controller import CategoriaController
from flask import jsonify, request, Blueprint

categoria_bp = Blueprint('categoria', __name__)

@categoria_bp.route("/categorias", methods=['GET'])
def get_all():
    try:
        categoria = CategoriaController.get_all()
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "No se encontraron categorias"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@categoria_bp.route("/categorias/<int:id>", methods=['GET'])
def get_one(id):
    try:
        categoria = CategoriaController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "Categoria no encontrada"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@categoria_bp.route('/categorias', methods=['POST'])
def create():
    try:
        data = request.get_json()
        categoria = CategoriaController.create(data)
        if categoria:
            return jsonify({"mensaje": "Categoria creada exitosamente"}), 201
        else:
            return jsonify({"mensaje": "No se pudo crear la categoria"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@categoria_bp.route('/categorias/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        categoria = CategoriaController.update(data)
        if categoria:
            return jsonify({"mensaje": "Categoria actualizada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo actualizar la categoria"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@categoria_bp.route('/categorias/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        categoria = CategoriaController.delete(id)
        if categoria:
            return jsonify({"mensaje": "Categoria eliminada exitosamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo eliminar la categoria"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500