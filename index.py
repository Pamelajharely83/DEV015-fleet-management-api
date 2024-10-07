"""
Este modulo contiene la inicialización de la aplicación
"""
from flask import Flask
from src.database.db import db
from src.routes.index_routes import main_routes
from src.routes.taxis_routes import taxis_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(taxis_routes)

if __name__ == '__main__':
    app.run(debug=True)
