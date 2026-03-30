from flask import Flask
from database.db import db
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  

    db.init_app(app)
    migrate.init_app(app, db)

    from routes.servicio_routes import servicio_routes
    from routes.citas_route import cita_routes
    

    app.register_blueprint(cita_routes, url_prefix='/api')
    app.register_blueprint(servicio_routes, url_prefix='/api')

    return app