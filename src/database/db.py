""" 
Este módulo crea la conexión con la base de datos
"""
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import create_engine
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('POSTGRES_URL')
if not DATABASE_URL:
    raise ValueError('No se ha encontrado la variable de entorno "POSTGRES_URL"')

db = SQLAlchemy()

# engine = create_engine(DATABASE_URL)
# Base = declarative_base()

# Session = sessionmaker(engine)
# session = Session()

def create_tables():
    """ Crea todas las tablas definidas en los modelos """
    try:
        # Base.metadata.create_all(engine)
        db.create_all()
        print('Tablas creadas con éxito')
    except* Exception as e:
        print(f'Error al crear las tablas {e}')

def delete_tables():
    """ Eliminar todas las tablas definidas en los modelos """
    try:
        # Base.metadata.drop_all(engine)
        db.drop_all()
        print('Tablas eliminadas con éxito')
    except* Exception as e:
        print(f'Error al eliminar las tablas {e}')

if __name__ == '__main__':
    delete_tables()
    create_tables()
