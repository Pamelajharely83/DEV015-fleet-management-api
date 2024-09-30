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

    taxis = db.session.query(Taxis).all()
    taxis_dict = [taxi.to_dict() for taxi in taxis]

    taxis_query_parameters = {
        'plate': request.args.get('plate'),
        'page': request.args.get('page', 1, type=int),
        'limit': request.args.get('limit', 10, type=int)
    }

    # 1era opción usando for
    # if taxis_query_parameters['plate'] is not None:
    #     for taxi in taxis:
    #         taxi_item = taxi.to_dict()
    #         if taxi_item['plate'] == taxis_query_parameters['plate']:
    #             return jsonify(taxi_item)
    #         return {'error': 'Taxi no encontrado'}

    #2da opcion usando next
    if taxis_query_parameters['plate']:
        taxi_item = next((
            taxi for taxi in taxis_dict
            if taxi['plate'] == taxis_query_parameters['plate']),
            {'error': 'Taxi no encontrado'}
        )

        return taxi_item
        # return {'error': 'Taxi no encontrado'}

    return taxis_dict
