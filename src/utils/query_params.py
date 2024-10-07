"""
Este módulo contiene los diccionarios de los parámetros de consulta para los servicios  
"""
from flask import request

# Se pasaron de diccionarios a funciones para evitar que se ejecuten antes de que la página exista (tenga una respuesta HTTP)
# y solo sean llamados cuando se necesiten

def get_taxi_query_params_for_paging():
    """ 
    Funcion que retorna el diccionario con las solicitudes a los 
    parametros de consulta para paginación
    """
    return {
        'page': request.args.get('page', 1, type=int),
        'limit': request.args.get('limit', 10, type=int)
    }

def get_taxi_query_params_for_filter():
    """ 
    Funcion que retorna el diccionario con las solicitudes a los 
    parametros de consulta para filtrar los elementos
    """
    return {
        'id': request.args.get('id'),
        'plate': request.args.get('plate'),
    }
