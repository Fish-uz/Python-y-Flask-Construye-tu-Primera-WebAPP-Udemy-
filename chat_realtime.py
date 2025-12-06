from flask import Flask, render_template
from flask_socketio import SocketIO

#TODO: Crear la aplicacion Flask
app = Flask(__name__)

#TODO: Configuracion de la clave secreta para sessiones
app.config["SECRET_KEY"] = "2356"

#TODO: Inicializar SocketIO con la aplicacion de FLASK
socketio = SocketIO(app)

