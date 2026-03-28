from flask import Blueprint, request, jsonify
from database.db import db
from models.citas import Cita
from datetime import datetime

cita_routes = Blueprint('cita', __name__)

# 🔹 GET ALL
@cita_routes.route('/citas', methods=['GET'])
def get_citas():
    citas = Cita.query.all()
    return jsonify([{
        "id": c.id,
        "servicio_id": c.servicio_id,
        "fecha_cita": str(c.fecha_cita),
        "hora_cita": str(c.hora_cita),
        "estado": c.estado
    } for c in citas]), 200


# 🔹 GET BY ID
@cita_routes.route('/citas/<int:id>', methods=['GET'])
def get_cita(id):
    cita = Cita.query.get(id)
    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    return jsonify({
        "id": cita.id,
        "servicio_id": cita.servicio_id,
        "fecha_cita": str(cita.fecha_cita),
        "hora_cita": str(cita.hora_cita),
        "estado": cita.estado
    }), 200


# 🔹 POST
@cita_routes.route('/citas', methods=['POST'])
def add_cita():
    data = request.json

    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    try:
        fecha = datetime.strptime(data['fecha_cita'], '%Y-%m-%d').date()
    except:
        return jsonify({"error": "Formato de fecha inválido (YYYY-MM-DD)"}), 400

    hora_raw = data.get('hora_cita', '')
    hora = None
    try:
        hora = datetime.strptime(hora_raw, '%H:%M:%S').time()
    except:
        try:
            hora = datetime.strptime(hora_raw, '%H:%M').time()
        except:
            return jsonify({"error": "Formato de hora inválido (HH:MM o HH:MM:SS)"}), 400

    nueva = Cita(
        servicio_id=data.get('servicio_id'),
        fecha_cita=fecha,
        hora_cita=hora,
        estado=data.get('estado')
    )

    db.session.add(nueva)
    db.session.commit()

    return jsonify({"mensaje": "Cita creada"}), 201


# 🔹 PUT
@cita_routes.route('/citas/<int:id>', methods=['PUT'])
def update_cita(id):
    cita = Cita.query.get(id)
    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    data = request.json

    try:
        cita.fecha_cita = datetime.strptime(data['fecha_cita'], '%Y-%m-%d').date()
    except:
        return jsonify({"error": "Formato de fecha inválido (YYYY-MM-DD)"}), 400

    hora_raw = data.get('hora_cita', '')
    try:
        cita.hora_cita = datetime.strptime(hora_raw, '%H:%M:%S').time()
    except:
        try:
            cita.hora_cita = datetime.strptime(hora_raw, '%H:%M').time()
        except:
            return jsonify({"error": "Formato de hora inválido (HH:MM o HH:MM:SS)"}), 400

    cita.servicio_id = data.get('servicio_id')
    cita.estado = data.get('estado')

    db.session.commit()

    return jsonify({"mensaje": "Cita actualizada"}), 200


# 🔹 DELETE
@cita_routes.route('/citas/<int:id>', methods=['DELETE'])
def delete_cita(id):
    cita = Cita.query.get(id)
    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    db.session.delete(cita)
    db.session.commit()

    return jsonify({"mensaje": "Cita eliminada"}), 200