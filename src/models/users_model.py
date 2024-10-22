""" 
Este módulo define el módelo de la tabla para los usuarios
"""
from sqlalchemy import Column, Integer, String
from src.database.db import db

class Users(db.Model):
    """ Modelo de tabla para los usuarios """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def to_dict(self):
        """
        Función para convertir los registros de la tabla en diccionarios
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    def __str__(self):
        return f'Name: {self.name}'
