from .presentacion_controller import PresentacionController
from flask import jsonify, request, Blueprint

presentacion_bp = Blueprint('presentacion', __name__)

@presentacion_bp.route("/presentacion", methods=['GET'])
def get_all():
    try:
        presentacion = PresentacionController.get_all()
        if presentacion:
            return jsonify(presentacion), 200
        else:
            return jsonify({"mensaje": "No se encontraron presentaciones"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@presentacion_bp.route("/presentacion/<int:id>", methods=['GET'])
def get_one(id):
    try:
        presentacion = PresentacionController.get_one(id)
        if presentacion:
            return jsonify(presentacion), 200
        else:
            return jsonify({"mensaje": "presentación no encontrada"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@presentacion_bp.route('/presentacion', methods=['POST'])
def create():
    try:
        data = request.get_json()
        presentacion = PresentacionController.create(data)
        if presentacion:
            return jsonify({"message": "Presentacion sabor creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear la presentación"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@presentacion_bp.route('/presentacion/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id
        presentacion = PresentacionController.update(data)
        if presentacion:
            return jsonify({"message": "Presentación actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar la presentación"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@presentacion_bp.route('/presentacion/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        presentacion = PresentacionController.delete(id)
        if presentacion:
            return jsonify({"message": "Presentación eliminada exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar la presentación"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500