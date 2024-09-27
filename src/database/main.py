""" 

"""
from src.database import db
from src.database.models import Taxis, Trajectories

if __name__ == '__main__':
    try:
        db.Base.metadata.drop_all(db.engine)
        db.Base.metadata.create_all(db.engine)
        print('Tablas eliminadas y creadas con éxito')
    except* Exception as e:
        print(f'Error al crear las tablas: {e}')
