from .precio_controller import PrecioController
from flask import jsonify, request, Blueprint

precio_bp = Blueprint('precio', __name__)

@precio_bp.route("/precios", methods=['GET'])
def get_all():
    try:
        precios = PrecioController.get_all()
        if precios:
            return jsonify(precios), 200
        else:
            return jsonify({"mensaje": "No se encontraron precios"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@precio_bp.route("/precios/<int:id>", methods=['GET'])
def get_one(id):
    try:
        precio = PrecioController.get_one(id)
        if precio:
            return jsonify(precio), 200
        else:
            return jsonify({"mensaje": "precio no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@precio_bp.route('/precios', methods=['POST'])
def create():
    try:
        data = request.get_json()
        precio = PrecioController.create(data)
        if precio:
            return jsonify({"message": "precio creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear el precio"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@precio_bp.route('/precios/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        precio = PrecioController.update(data)
        if precio:
            return jsonify({"message": "precio actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el precio"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@precio_bp.route('/precios/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        precio = PrecioController.delete(id)
        if precio:
            return jsonify({"message": "precio eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar el precio"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500