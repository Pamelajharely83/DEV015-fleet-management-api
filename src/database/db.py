""" 
Este módulo crea la conexión con la base de datos
"""
import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('POSTGRES_URL', 'Variable no encontrada')

engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(engine)
session = Session()
