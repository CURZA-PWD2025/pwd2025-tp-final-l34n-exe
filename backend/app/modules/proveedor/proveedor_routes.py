from .proveedor_controller import ProveedorController
from flask import jsonify, request, Blueprint

proveedor_bp = Blueprint('proveedor', __name__)

@proveedor_bp.route("/proveedores", methods=['GET'])
def get_all():
    try:
        proveedores = ProveedorController.get_all()
        if proveedores:
            return jsonify(proveedores), 200
        else:
            return jsonify({"mensaje": "No se encontraron proveedores"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@proveedor_bp.route("/proveedores/<int:id>", methods=['GET'])
def get_one(id:int):
    try:
        proveedor = ProveedorController.get_one(id)
        if proveedor:
            return jsonify(proveedor), 200
        else:
            return jsonify({"mensaje": "proveedor no encontrado"}), 404
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@proveedor_bp.route('/proveedores', methods=['POST'])
def create():
    try:
        data = request.get_json()
        proveedor = ProveedorController.create(data)
        if proveedor:
            return jsonify({"message": "proveedor creado exitosamente"}), 201
        else:
            return jsonify({"message": "No se pudo crear el proveedor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@proveedor_bp.route('/proveedores/<int:id>', methods=['PUT'])
def update(id:int):
    try:
        data = request.get_json()
        data['id'] = id
        proveedor = ProveedorController.update(data)
        if proveedor:
            return jsonify({"message": "proveedor actualizado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el proveedor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

@proveedor_bp.route('/proveedores/<int:id>', methods=['DELETE'])
def delete(id:int):
    try:
        proveedor = ProveedorController.delete(id)
        if proveedor:
            return jsonify({"message": "proveedor eliminado exitosamente"}), 200
        else:
            return jsonify({"message": "No se pudo eliminar el proveedor"}), 500
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500