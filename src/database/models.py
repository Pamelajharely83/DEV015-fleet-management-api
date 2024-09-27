"""
Este módulo define las tablas de la base de datos para el sistema de gestión de flotas.
Incluye:
- Módelo de tabla para los taxis
- Módelo de tabla para las trayectorias
"""
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from src.database import db

class Taxis(db.Base):
    """ Modelo de tabla para los taxis """
    __tablename__ = 'taxis'

    id = Column(Integer, primary_key=True)
    plate = Column(String, nullable=False)

    def __str__(self):
        return f'Trajectory ID: {self.plate}'

class Trajectories(db.Base):
    """ Modelo de tabla para las trayectorias """
    __tablename__ = 'trajectories'

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey('taxis.id'))
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    latitude = Column(Float)
    longitude = Column(Float)

    def __str__(self):
        return f'Taxi ID: {self.taxi_id}'