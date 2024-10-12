""" 
Este modulo contiene la ruta a /trajectories y sus configuraciones
"""
from flask import Blueprint
from src.database.db import db
from src.models.trajectories_models import Trajectories
from src.services.list_data import filter_by_query_param, paginate_data, filter_set
from src.services.response_status import handle_list_response, validate_paging_param
from src.utils.query_params import get_trajectory_query_params_for_filter, get_query_params_for_paging

trajectories_routes = Blueprint('trajectories_routes', __name__)

@trajectories_routes.route('/trajectories')

def fetch_trajectories():
    """
    Función para obtener las trayectorias de los taxis de la base de datos
    (de forma predeterminada muestra un listado de los 10 primeros elementos)
    Se puede filtrar por ID y date (individual y de forma conjunta) según
    parámetros de consulta
    """
    params_for_filter = get_trajectory_query_params_for_filter()
    params_for_paging = get_query_params_for_paging()

    filtered_trajectories_by_taxiid = filter_by_query_param(db, Trajectories, Trajectories.taxi_id,
    params_for_filter['taxiId'], Trajectories.to_dict)
    filtered_trajectories_by_date = filter_by_query_param(db, Trajectories, Trajectories.date,
    params_for_filter['date'], Trajectories.to_dict)
    
    if params_for_filter['taxiId'] and params_for_filter['date']:
        if filtered_trajectories_by_taxiid:
            trajectories_by_id = filter_set(filtered_trajectories_by_taxiid, 'date', params_for_filter['date'])
            return handle_list_response(trajectories_by_id,
            f'Taxi(s) con id "{str(params_for_filter['taxiId'])}" y fecha "{str(params_for_filter["date"])}" no encontrado(s)')
        if filtered_trajectories_by_date:
            trajectories_by_date = filter_set(filtered_trajectories_by_date, 'taxiId', params_for_filter['taxiId'])
            return handle_list_response(trajectories_by_date,
            f'Taxi(s) con id "{str(params_for_filter['taxiId'])}" y fecha "{str(params_for_filter["date"])}" no encontrado(s)')

    if params_for_filter['date']:
        return handle_list_response(filtered_trajectories_by_date,
        f'Trayectoria(s) con fecha "{str(params_for_filter['date'])}" no encontrado(s)')
    if params_for_filter['taxiId']:
        return handle_list_response(filtered_trajectories_by_taxiid,
        f'Taxi(s) con id "{str(params_for_filter['taxiId'])}" no encontrado(s)')

    validate_paging_param(params_for_paging['page'], 400)
    validate_paging_param(params_for_paging['limit'], 400)

    paginated_trajectories = paginate_data(Trajectories, params_for_paging['page'],
    params_for_paging['limit'], params_for_filter)

    return handle_list_response([Trajectories.to_dict(item) for item in paginated_trajectories],
    'Error al obtener la lista', 404)
