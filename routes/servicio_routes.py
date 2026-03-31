from flask import Blueprint, request, jsonify
from database.db import db
from models.servicio import Servicio
from datetime import datetime

servicio_routes = Blueprint('servicio', __name__)

# 🔹 GET ALL
@servicio_routes.route('/servicios', methods=['GET'])
def get_servicios():
    servicios = Servicio.query.all()
    return jsonify([{
        "id": s.id,
        "nombre_servicio": s.nombre_servicio,
        "precio": s.precio
    } for s in servicios]), 200


# 🔹 GET BY ID
@servicio_routes.route('/servicios/<int:id>', methods=['GET'])
def get_servicio(id):
    servicio = Servicio.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404

    return jsonify({
        "id": servicio.id,
        "nombre_servicio": servicio.nombre_servicio,
        "precio": servicio.precio
    }), 200


# 🔹 POST
@servicio_routes.route('/servicios', methods=['POST'])
def add_servicio():
    data = request.json

    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    nuevo = Servicio(
        nombre_servicio=data.get('nombre_servicio'),
        precio=data.get('precio')
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({"mensaje": "Servicio creado"}), 201


# 🔹 PUT
@servicio_routes.route('/servicios/<int:id>', methods=['PUT'])
def update_servicio(id):
    servicio = Servicio.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404

    data = request.json

    servicio.nombre_servicio = data.get('nombre_servicio')
    servicio.precio = data.get('precio')

    db.session.commit()

    return jsonify({"mensaje": "Servicio actualizado"}), 200


# 🔹 DELETE
@servicio_routes.route('/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):
    servicio = Servicio.query.get(id)
    if not servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404

    db.session.delete(servicio)
    db.session.commit()

    return jsonify({"mensaje": "Servicio eliminado"}), 200