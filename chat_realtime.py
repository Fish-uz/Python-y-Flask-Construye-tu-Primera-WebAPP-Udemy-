from flask import Flask, render_template
from flask_socketio import SocketIO

#TODO: Crear la aplicacion Flask
app = Flask(__name__)

#TODO: Configuracion de la clave secreta para sessiones
app.config["SECRET_KEY"] = "2356"

#TODO: Inicializar SocketIO con la aplicacion de FLASK
socketio = SocketIO(app) 

@app.route('/')

def index():
    return render_template('chat_realtime.html', mensajes=[], nombre='Invitado')

@socketio.on('mensaje')
def manejar_mensaje(data):
    #TODO Obtener el nombre y el nuevo mensaje del diccionario "data"
    nombre = data['nombre']
    nuevo_mensaje = data['mensaje']

# TODO: Emitir un evento actualizar_mensaje a todos los clientes conectados
    socketio.emit('actualizar_mensajes',{'nombre': nombre,'mensaje': nuevo_mensaje})

#TODO: Ejecutar la aplicacion Flask con el servidor SocketIO en modo depuracion
if __name__ == '__main__':
    socketio.run(app,debug=True)