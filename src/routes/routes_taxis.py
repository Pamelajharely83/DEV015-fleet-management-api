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
        'id': request.args.get('id'),
        'plate': request.args.get('plate'),
        'page': request.args.get('page', 1, type=int),
        'limit': request.args.get('limit', 10, type=int)
    }

    #? PARA OBTENER LISTADO DE TAXIS POR ID
    if taxis_query_parameters['id']:
        taxis_by_id = [taxi for taxi in taxis_dict if str(taxis_query_parameters['id']) in str(taxi['id'])]
        if taxis_by_id:
            return jsonify(taxis_by_id)
        return {'error': f'Taxi(s) con id "{str(taxis_query_parameters['id'])}" no encontrado(s)'}, 404

    #? PARA OBTENER LISTADO DE TAXIS POR PLACA:
    if taxis_query_parameters['plate']:
        taxis_by_plate = [taxi for taxi in taxis_dict if taxis_query_parameters['plate'].lower() in taxi['plate'].lower()]
        if taxis_by_plate:
            return jsonify(taxis_by_plate)
        return {'error': f'Taxi con placa "{taxis_query_parameters["plate"]}" no encontrado'}, 404

    #? PARA OBTENER LISTADO DE TAXIS POR PÁGINA Y LIMITE:
    if taxis_query_parameters['id'] is None and taxis_query_parameters['plate'] is None:
        offset_value_taxis = db_taxis.offset((taxis_query_parameters['page'] - 1) * taxis_query_parameters['limit'])
        limit_taxis = offset_value_taxis.limit(taxis_query_parameters['limit']).all()
        taxis_per_page = [taxi_per_page.to_dict() for taxi_per_page in limit_taxis]
        return jsonify(taxis_per_page)
