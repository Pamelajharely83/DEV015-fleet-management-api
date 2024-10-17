""" 
Este modulo contiene la ruta a /users y sus configuraciones
"""
from flask import Blueprint, request, jsonify

users_routes = Blueprint('users_routes', __name__)

@users_routes.route('/users', methods=['GET', 'POST'])
def create_users():
    try:
        # print(request.json)
        return jsonify({'message': 'Usuario registrado'})
    except Exception as ex:
        return jsonify({'error': 'Error', 'detail': ex})
