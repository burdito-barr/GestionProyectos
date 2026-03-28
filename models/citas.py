from database.db import db

class Cita(db.Model):
    __tablename__ = 'Cita'

    id = db.Column(db.Integer, primary_key=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('Servicio.id'), nullable=False)
    fecha_cita = db.Column(db.Date, nullable=False)
    hora_cita = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(50), nullable=False)