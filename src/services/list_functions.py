""" 
Este modulo contiene las funciones 
para obtener una lista de elementos 
de la base de datos 
"""
from flask import jsonify

def filter_by_query_param(query_param, item_attribute, items_list):
    """
    Filtra los elementos de la data por el parametro de consulta
    y retorna la lista filtrada.

    Argumento(s):
    - query_param: Parametro de consulta existente
    - item_attribute: Propiedad que se comparará con el query param para el filtrado
    - items_list: Lista de los elementos a filtrar
    """

    filtered_items = [item for item in items_list if str(query_param).lower() in str(item[item_attribute]).lower()]
    return filtered_items

def handle_list_response(items_list, message_error, error_code=404):
    """
    Verifica si la operación ha devuelto resultados
    En caso de que sí, devuelve la lista de diccionarios en formato JSON
    Si no, devuelve un error con mensaje personalizado
    
    Argumento(s):
    - items_list: Lista con los diccionarios
    - message_error: Mensaje para describir el error
    - error_code: Código de error a mostrar (por defecto, 404)
    """
    if items_list:
        return jsonify(items_list), 200
    return {'message': message_error}, error_code

def paginate_data(database, query_page, query_limit, filter_query_params, dict_converter):
    """
    Verifica que no existan parametros de filtrado activos y
    retorna los elementos paginados.

    Argumento(s):
    - database: Conexión a la base de datos con la tabla a paginar
    - query_page: Número de página
    - query_limit: Número limite de consultas a mostrar por página
    - filter_query_params: Diccionario con los parámetros de filtrado
    - dict_converter: Función para convertir los registros de la tabla en diccionario
    """
    if all(value is None for value in filter_query_params.values()):
        offset_value = database.offset((query_page - 1) * query_limit)
        items_paginated = offset_value.limit(query_limit).all()
        return [dict_converter(item) for item in items_paginated]
    return None
