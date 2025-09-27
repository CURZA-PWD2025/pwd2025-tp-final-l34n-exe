from .producto_controller import ProductoController
from flask import jsonify, request, Blueprint

producto_bp = Blueprint('producto', __name__)

@producto_bp.route("/producto", methods=['GET'])
def get_all():
    try:
        productos = ProductoController.get_all()
        if productos:
            return jsonify(productos), 200
        else:
            return jsonify({"mensaje": "No se encontraron productos"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@producto_bp.route("/producto/<int:id>", methods=['GET'])
def get_one(id):
    try:
        producto = ProductoController.get_one(id)
        if producto:
            return jsonify(producto), 200
        else:
            return jsonify({"mensaje": "Producto no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@producto_bp.route('/producto', methods=['POST'])
def create():
    try:
        data = request.get_json()
        producto = ProductoController.create(data)
        if producto:
            return jsonify({"message": "Producto creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear el producto"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@producto_bp.route('/producto/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        producto = ProductoController.update(data)
        if producto:
            return jsonify({"message": "Producto actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el producto"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@producto_bp.route('/producto/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        producto = ProductoController.delete(id)
        if producto:
            return jsonify({"message": "Producto eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar el producto"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500