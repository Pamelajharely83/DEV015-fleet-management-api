from src.routes.trajectories_routes import trajectories_routes

@trajectories_routes.route('/trajectories/latest')
def fetch_latest_trajectories():
    return {'message': 'Hola, soy /trajectories/latest'}
