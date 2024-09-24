"""
Este módulo define las tablas de la base de datos para el sistema de gestión de flotas.
Incluye:
- Módelo de tabla para los taxis
- Módelo de tabla para las trayectorias
"""
import os
from datetime import datetime, timezone
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('POSTGRES_URL', 'Variable no encontrada')

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Taxis(Base):
    """ Modelo de tabla para los taxis """
    __tablename__ = 'taxis'

    id = Column(Integer, primary_key=True)
    plate = Column(String, nullable=False, unique=True)

    def __str__(self):
        return f'Trajectory ID: {self.plate}'

class Trajectories(Base):
    """ Modelo de tabla para las trayectorias """
    __tablename__ = 'trajectories'

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey('taxis.id'))
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    latitude = Column(Float)
    longitude = Column(Float)

    def __str__(self):
        return f'Taxi ID: {self.taxi_id}'

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print('Tablas eliminadas y creadas con éxito')
    except* Exception as e:
        print(f'Error al crear las tablas: {e}')
