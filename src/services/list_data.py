""" 
Este modulo contiene las funciones 
para obtener una lista de elementos 
de la base de datos 
"""
from sqlalchemy import select, cast, String
from flask import abort, request

def filter_set(item_list, key, search_value):
    """
    Itera una lista de objetos a filtrar y retorna la lista si el valor 
    buscado coincide parcial o enteramente con el valor de la key dada

    Argumento(s):
    - item_list: Lista de objetos
    - key: Llave que contiene el valor para el filtrado
    - search_value: Valor buscado
    """
    def iterator_func(x):
        if str(search_value) in str(x[key]):
            return True
        return False
    return list(filter(iterator_func, item_list))

def filter_by_query_param(database, model, column, query_param, dict_converter):
    """
    Filtra los elementos de la data por el parametro de consulta
    y retorna la lista filtrada.

    Argumento(s):
    - database: Base de datos
    - Model: Modelo de tabla a filtrar
    - column: Columna con la que se hará el filtrado
    - query_param: Parámetro de filtrado
    - dict_converter: Función que convierte cada instancia en un diccionario
    """
    filtered_data = select(model).where(cast(column, String).ilike(f'%{query_param}%'))
    query_execution = database.session.execute(filtered_data).scalars()

    return [dict_converter(item) for item in query_execution.all()]

def paginate_data(model, query_page, page_default, query_limit, limit_default):
    """
    Verifica que no existan parametros de filtrado activos y
    retorna los elementos paginados.

    Argumento(s):
    - model: Modelo de tabla
    - query_page: Nombre del párametro de consulta para la página
    - page_default: Valor por defecto para el número de página
    - query_limit: Nombre del párametro de consulta para el limite de elementos a mostrar
    - limit_default: Valor por defecto para el número limite
    - filter_query_params: Diccionario con los parámetros de filtrado
    """

    page = request.args.get(query_page, page_default)
    limit = request.args.get(query_limit, limit_default)

    if not str(page).isdigit() or not str(limit).isdigit():
        invalid_value = page if not str(page).isdigit() else limit
        abort(400, description= f'Valor ingresado "{invalid_value}" no válido, por favor ingresar un valor numérico')

    paginated_data = model.query.paginate(page=int(page), per_page=int(limit))
    return paginated_data.items
