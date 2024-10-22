"""
Este modulo contiene la inicialización de la aplicación
"""
from sqlalchemy import inspect, text
from flask import Flask
from src.database.db import db
from src.routes.index_routes import main_routes
from src.routes.taxis_routes import taxis_routes
from src.routes.trajectories_routes import trajectories_routes
from src.routes.trajectories_latest_routes import trajectories_routes
from src.routes.users_routes import users_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(taxis_routes)
app.register_blueprint(trajectories_routes)
app.register_blueprint(users_routes)

def create_tables():
    """ Crea todas las tablas definidas en los modelos """
    try:
        db.create_all()
        print('Tablas creadas con éxito')
    except Exception as e:
        print(f'Error al crear las tablas {e}')

def delete_tables():
    """ Eliminar todas las tablas definidas en los modelos """
    try:
        inspector = inspect(db.engine)
        tables = db.metadata.tables.keys()

        for table in tables:
            if inspector.has_table(table):
                drop_query = text(f'DROP TABLE {table} CASCADE')
                db.session.execute(drop_query)
                # db.metadata.tables[table].drop(db.engine, checkfirst=True, cascade=True)
                print(f'Tabla {table} eliminada con éxito')
            else:
                print(f'La tabla {table} no existe, así que no se elimina')
    except Exception as e:
        print(f'Error al eliminar las tablas {e}')

if __name__ == '__main__':
    app.run(debug=True)
