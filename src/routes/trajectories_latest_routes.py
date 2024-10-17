""" 
Este modulo contiene la ruta a /trajectories/latest y sus configuraciones
"""
from sqlalchemy import select, join
from sqlalchemy.orm import aliased
from flask import jsonify
from src.routes.trajectories_routes import trajectories_routes
from src.models.trajectories_models import Trajectories
from src.models.taxis_model import Taxis
from src.database.db import db

@trajectories_routes.route('/trajectories/latest')
def fetch_latest_trajectories():
    """
    Función para obtener las últimas trayectorias de cada taxi de la base de datos
    """
    t1 = aliased(Trajectories)
    t2 = aliased(Taxis)

    sub_query_taxis = (
        select(t2)
        .alias('taxis_alias')
    )

    query_trajectories = (
        select(t1.taxi_id, t1.date, t1.latitude, t1.longitude, t2.plate)
        .distinct(t1.taxi_id)
        .join(
            sub_query_taxis, t1.taxi_id == sub_query_taxis.c.id
        )
        .order_by(
            t1.taxi_id, t1.date.desc()
        )
    )
    execute_query = db.session.execute(query_trajectories).all()

    latest_trajectories = [
        {'taxiId': item.taxi_id, 'date': item.date, 'latitude': item.latitude, 'longitude': item.longitude, 'plate': item.plate}
        for item in execute_query
    ]

    return jsonify(latest_trajectories)
