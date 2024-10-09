""" Este modulo contiene las funciones para el manejo de estados de respuesta """
from flask import jsonify

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
    return {'error': message_error}, error_code

def validate_paging_param(query_param, error_code=400):
    """
    Verifica si el párametro de consulta es un número
    
    Argumento(s):
    - query_param: Párametro para la páginación
    - error_code: Código de error a mostrar (por defecto, 400)
    """
    if not str(query_param).isdigit():
        return {'error': f'Valor ingresado "{query_param}" no válido, por favor ingresar un valor numérico'}, error_code
    return None
