""" 
Este módulo define las tablas de la base de datos para el sistema de gestión de flotas.
Incluye:
- Módelo de tabla para los taxis 
"""

from sqlalchemy import Column, Integer, String
from src.database.db import db

class Taxis(db.Model):
    """ Modelo de tabla para los taxis """
    __tablename__ = 'taxis'

    id = Column(Integer, primary_key=True)
    plate = Column(String, nullable=False)

    def to_dict(self):
        """
        Función para convertir los registros de la tabla en diccionarios
        """
        return {
            'id': self.id,
            'plate': self.plate
        }

    def __str__(self):
        return f'Taxi ID: {self.plate}'
