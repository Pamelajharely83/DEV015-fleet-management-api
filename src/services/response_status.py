""" Este modulo contiene las funciones para el manejo de estados de respuesta """
from flask import jsonify, abort

def handle_list_response(result, message_error, error_code=404):
    """
    Verifica si la operación ha devuelto resultados
    En caso de que sí, devuelve las instancias convertidas en objetos en formato JSON
    Si no, devuelve un mensaje de error personalizado
    
    Argumento(s):
    - result: Lista devuelta por una operación
    - message_error: Mensaje para describir el error
    - error_code: Código de error a mostrar (por defecto, 404)
    """
    if not result:
        return {'error': message_error}, error_code
    return jsonify(result), 200

def validate_paging_param(query_param, error_code=400):
    """
    Verifica si el párametro de consulta es un número
    
    Argumento(s):
    - query_param: Párametro para la páginación
    - error_code: Código de error a mostrar (por defecto, 400)
    """
    if not str(query_param).isdigit():
        abort(error_code, description=f'Valor ingresado "{query_param}" no válido, por favor ingresar un valor numérico')
    return None
