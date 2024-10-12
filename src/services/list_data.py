""" 
Este modulo contiene las funciones 
para obtener una lista de elementos 
de la base de datos 
"""
from sqlalchemy import select, cast, String

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
        if search_value in str(x[key]):
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

def paginate_data(model, query_page, query_limit, filter_query_params):
    """
    Verifica que no existan parametros de filtrado activos y
    retorna los elementos paginados.

    Argumento(s):
    - model: Modelo de tabla
    - query_page: Número de página
    - query_limit: Número limite de consultas a mostrar por página
    - filter_query_params: Diccionario con los parámetros de filtrado
    """
    if all(value is None for value in filter_query_params.values()):
        paginated_data = model.query.paginate(page=query_page, per_page=query_limit)
        return paginated_data.items
    return None
