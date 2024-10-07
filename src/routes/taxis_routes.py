"""
Este modulo contiene la ruta a /taxis 
"""
from flask import Blueprint
from src.database.db import db
from src.models.taxis_model import Taxis
from src.services.list_functions import paginate_data, handle_list_response, filter_by_query_param
from src.utils.query_params import get_taxi_query_params_for_filter, get_taxi_query_params_for_paging

taxis_routes = Blueprint('taxis_routes', __name__)

@taxis_routes.route('/taxis')
def fetch_taxis():
    """
    Función para obtener los taxis de la base de datos
    (de forma predeterminada muestra un listado de los 10 primeros elementos)
    Se puede filtrar por ID y placa según parámetros de consulta
    """
    db_taxis = db.session.query(Taxis)
    taxis_dict = [taxi.to_dict() for taxi in db_taxis.all()]

    query_params_for_filter = get_taxi_query_params_for_filter()
    query_params_for_paging = get_taxi_query_params_for_paging()

    if query_params_for_filter['id']:
        filtered_taxis_by_id = filter_by_query_param(query_params_for_filter['id'],
        'id', taxis_dict)
        return handle_list_response(filtered_taxis_by_id, 
        f'Taxi(s) con id "{str(query_params_for_filter['id'])}" no encontrado(s)')

    if query_params_for_filter['plate']:
        filtered_taxis_by_plate = filter_by_query_param(query_params_for_filter['plate'],
        'plate', taxis_dict)
        return handle_list_response(filtered_taxis_by_plate, 
        f'Taxi con placa "{query_params_for_filter['plate']}" no encontrado')

    paginated_taxis = paginate_data(db_taxis, query_params_for_paging['page'],
    query_params_for_paging['limit'], query_params_for_filter, Taxis.to_dict)

    return handle_list_response(paginated_taxis, 'Error al obtener la lista')
