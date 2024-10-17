""" 
Este módulo define las tablas de la base de datos para el sistema de gestión de flotas.
Incluye:
- Módelo de tabla para las trayectorias
"""
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from src.database.db import db

class Trajectories(db.Model):
    """ Modelo de tabla para las trayectorias """
    __tablename__ = 'trajectories'

    id = Column(Integer, primary_key=True)
    taxi_id = Column(Integer, ForeignKey('taxis.id'))
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    latitude = Column(Float)
    longitude = Column(Float)

    def to_dict(self):
        """
        Función para convertir los registros de la tabla en diccionarios
        """
        return {
            'id': self.id,
            'taxiId': self.taxi_id,
            'date': self.date,
            'latitude': self.latitude,
            'longitude': self.longitude
        }

    def __str__(self):
        return f'Trajectory ID: {self.taxi_id}'
