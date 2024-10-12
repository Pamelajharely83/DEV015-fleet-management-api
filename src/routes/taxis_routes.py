"""
Este modulo contiene la ruta a /taxis y sus configuraciones
"""
from flask import Blueprint
from src.database.db import db
from src.models.taxis_model import Taxis
from src.services.list_data import paginate_data, filter_by_query_param
from src.services.response_status import handle_list_response, validate_paging_param
from src.utils.query_params import get_taxi_query_params_for_filter, get_query_params_for_paging

taxis_routes = Blueprint('taxis_routes', __name__)

@taxis_routes.route('/taxis')
def fetch_taxis():
    """
    Función para obtener los taxis de la base de datos
    (de forma predeterminada muestra un listado de los 10 primeros elementos)
    Se puede filtrar por ID y placa según parámetros de consulta
    """
    params_for_filter = get_taxi_query_params_for_filter()
    params_for_paging = get_query_params_for_paging()

    if params_for_filter['plate']:
        filtered_taxis_by_plate = filter_by_query_param(db, Taxis, Taxis.plate,
        params_for_filter['plate'])
        return handle_list_response(filtered_taxis_by_plate, Taxis.to_dict,
        f'Taxi(s) con placa "{str(params_for_filter['plate'])}" no encontrado(s)', 404)

    if params_for_filter['id']:
        filtered_taxis_by_id = filter_by_query_param(db, Taxis, Taxis.id,
        params_for_filter['id'])
        return handle_list_response(filtered_taxis_by_id, Taxis.to_dict,
        f'Taxi(s) con id "{str(params_for_filter['id'])}" no encontrado(s)', 404)

    validate_paging_param(params_for_paging['limit'], 400)
    validate_paging_param(params_for_paging['page'], 400)

    paginated_taxis = paginate_data(Taxis, params_for_paging['page'],
    params_for_paging['limit'], params_for_filter)

    return handle_list_response(paginated_taxis.items, Taxis.to_dict,
    'Error al obtener la lista', 404)
