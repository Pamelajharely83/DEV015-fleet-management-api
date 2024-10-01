""" 
Este modulo usa flask para crear una aplicación simple que imprima 'Hi hi, world c:' en el navegador 
"""
from flask import Flask, request, jsonify
from src.database import db
from src.database.models import Taxis, Trajectories

app = Flask(__name__)

@app.route('/')
def get_entire_database():
    """ 
    Función que imprime toda la base de datos 
    (registros de Taxis y Trajectories) 
    en el navegador en formato JSON 
    """
    database_taxis = db.session.query(Taxis).all()
    database_trajectories = db.session.query(Trajectories).all()
    db_taxis_dict = [taxi.to_dict() for taxi in database_taxis]
    db_trajectories_dict = [trajectory.to_dict() for trajectory in database_trajectories]

    return jsonify({'Taxis': db_taxis_dict, 'Trayectorias': db_trajectories_dict})

@app.route('/taxis')
def fetch_taxis():
    """ 
    Función para obtener todos 
    los taxis de la base de datos 
    """
    db_taxis = db.session.query(Taxis)
    taxis_dict = [taxi.to_dict() for taxi in db_taxis.all()]

    taxis_query_parameters = {
        'id': request.args.get('id', None, type=int),
        'plate': request.args.get('plate'),
        'page': request.args.get('page', None, type=int),
        'limit': request.args.get('limit', None, type=int)
    }
    #? PARA OBTENER LISTADO DE TAXIS POR ID
    if taxis_query_parameters['id']:
        taxi_item_by_id = next((
                            taxi for taxi in taxis_dict
                            if taxi['id'] == taxis_query_parameters['id'])
                            , None)
        if taxi_item_by_id:
            return jsonify(taxi_item_by_id)
        return {'error': f'Taxi con id "{taxis_query_parameters['id']}" no encontrado'}, 404

    #? PARA OBTENER LISTADO DE TAXIS POR PLACA:
    if taxis_query_parameters['plate']:
        taxi_item = next((
                    taxi for taxi in taxis_dict
                    if taxi['plate'] == taxis_query_parameters['plate']),
                    None)
        if taxi_item:
            return jsonify(taxi_item)
        return {'error': f'Taxi con placa "{taxis_query_parameters["plate"]}" no encontrado'}, 404

    #? PARA OBTENER LISTADO DE TAXIS POR PÁGINA Y LIMITE:
    if taxis_query_parameters['page'] and taxis_query_parameters['limit']:
        offset_value_taxis = db_taxis.offset((taxis_query_parameters['page'] - 1) * taxis_query_parameters['limit'])
        limit_taxis = offset_value_taxis.limit(taxis_query_parameters['limit']).all()
        taxis_per_page = [taxi_per_page.to_dict() for taxi_per_page in limit_taxis]
        return jsonify(taxis_per_page)

    # si limit tiene un valor pero no page entonces debe retornar la cantidad de taxis por limite
    if taxis_query_parameters['limit'] and taxis_query_parameters['page'] is None:
        taxis_limit = db_taxis.limit(taxis_query_parameters['limit']).all()
        taxis_per_limit = [taxi_per_limit.to_dict() for taxi_per_limit in taxis_limit]
        return jsonify(taxis_per_limit)

    # si existe page pero no limit debería arrojar un error mencionando que no se mencionó el límite
    if taxis_query_parameters['page'] and taxis_query_parameters['limit'] is None:
        return {'error': f'No se especificó la cantidad de elementos a mostrar (limit={taxis_query_parameters["limit"]})'}, 404
    # si no existe valor en page ni limit debe retornar todos los taxis

    #? Colocando el limite
    # taxis_per_page = []
    # if taxis_query_parameters['limit']:
    #     for i, taxi_per_page in enumerate(taxis_dict):
    #         if i < taxis_query_parameters['limit']:
    #             taxis_per_page.append(taxi_per_page)
    #     return jsonify(taxis_per_page)
    return jsonify(taxis_dict)
