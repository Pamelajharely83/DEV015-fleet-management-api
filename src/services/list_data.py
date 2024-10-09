""" 
Este modulo contiene las funciones 
para obtener una lista de elementos 
de la base de datos 
"""

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
        offset_value = database.offset((int(query_page) - 1) * int(query_limit))
        items_paginated = offset_value.limit(int(query_limit)).all()
        return [dict_converter(item) for item in items_paginated]
    return None
