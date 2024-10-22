"""
Ejecuta las funciones para eliminar y crear las tablas
"""

from index import app, create_tables, delete_tables

if __name__ == '__main__':
    with app.app_context():
        delete_tables()
        create_tables()
