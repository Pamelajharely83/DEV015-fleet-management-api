""" 
Este módulo crea la conexión con la base de datos
"""
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('POSTGRES_URL')
if not DATABASE_URL:
    raise ValueError('No se ha encontrado la variable de entorno "POSTGRES_URL"')

db = SQLAlchemy()
