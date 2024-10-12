""" 
Este modulo contiene las funciones 
para obtener una lista de elementos 
de la base de datos 
"""
from sqlalchemy import select, cast, String

def filter_by_query_param(database, model, column, query_param):
    """
    Filtra los elementos de la data por el parametro de consulta
    y retorna la instancia filtrada.

    Argumento(s):
    - database: Base de datos
    - Model: Modelo de tabla a filtrar
    - column: Columna con la que se hará el filtrado
    - query_param: Parámetro de filtrado
    """
    filtered_data = select(model).where(cast(column, String).ilike(f'%{query_param}%'))
    query_execution = database.session.execute(filtered_data).scalars()

    return query_execution.all()

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
        return paginated_data
    return None
