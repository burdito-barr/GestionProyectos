from database.db import db

class Cita(db.Model):
    __tablename__ = 'Cita'

    id = db.Column(db.Integer, primary_key=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('Servicio.id'), nullable=False)
    fecha_cita = db.Column(db.Date, nullable=False)
    hora_cita = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    servicio = db.relationship('Servicio')

def serialize_cita(cita):
    return {
        "id": cita.id,
        "fecha_cita": str(cita.fecha_cita),
        "hora_cita": str(cita.hora_cita),
        "estado": cita.estado,
        "servicio": {
            "id": cita.servicio.id,
            "nombre_servicio": cita.servicio.nombre_servicio
        } if cita.servicio else None
    }