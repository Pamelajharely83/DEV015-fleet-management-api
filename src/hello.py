""" 
Este modulo usa flask para crear una aplicación simple que imprima 'Hi hi, world c:' en el navegador 
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Función que imprime un saludo en el navegador """
    return '<p>Hi hi, world c: </p>'

@app.route('/taxis', methods=['GET', 'POST'])
def method_get():
    """ Función para probar métodos HTTP """
    if request.method == 'GET':
        return '<p>Holi, usando un método GET</p>'
