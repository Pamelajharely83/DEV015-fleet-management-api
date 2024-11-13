""" 
Este modulo contiene la ruta a /users y sus configuraciones
"""
from flask import Blueprint, jsonify
from src.services.list_data import paginate_data
from src.services.response_status import handle_list_response
from src.models.users_model import Users

users_routes = Blueprint('users_routes', __name__)

@users_routes.errorhandler(400)
def bad_request(error):
    """
    Función para manejar las respuestas de estado 400
    """
    return jsonify({'error': error.description}), 400

@users_routes.route('/users')
def fetch_users():
    """
    Función para obtener los usuarios de la base de datos
    (de forma predeterminada muestra un listado de los 10 primeros elementos
    """
    paginated_users = paginate_data(Users, 'page', 1, 'limit', 10)
    return handle_list_response([Users.to_dict(user) for user in paginated_users],
    'Error al obtener la lista', 404)

# @users_routes.route('/users', methods=['POST'])
# def create_users():
#     try:
#         # print(request.json)
#         return jsonify({'message': 'Usuario registrado'})
#     except Exception as ex:
#         return jsonify({'error': 'Error', 'detail': ex})
