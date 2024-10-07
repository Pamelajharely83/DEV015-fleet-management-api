""" Este modulo contiene la ruta de la página principal """
from flask import Blueprint

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    """ Ruta a la página de inicio """
    return '<h1>Bienvenid@ a Fleet Management API</h1><p>Tienes disponible las rutas "/taxis" y "/trajectories"</p>'

@main_routes.app_errorhandler(404)
def not_found_error(error):
    """ Página de error 404 """
    return {'error': 'Página no encontrada, prueba con otra ruta', 'message': str(error)}, 404
