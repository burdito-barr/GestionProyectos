from database.db import db

class Servicio(db.Model):
    __tablename__ = 'Servicio'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, nullable=False)  # ⚠️ quitamos FK inválida
    nombre_servicio = db.Column(db.String(150), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    citas = db.relationship('Cita', backref='servicio', lazy=True)