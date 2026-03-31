from database.db import db

class Servicio(db.Model):
    __tablename__ = 'Servicio'

    id = db.Column(db.Integer, primary_key=True)
    nombre_servicio = db.Column(db.String(150), nullable=False)
    precio = db.Column(db.Float, nullable=False)



