from flask import Flask
from flask_socketio import SocketIO, emit

def routeHandler():
    pass

class SocketIOServer:
    
    def __init__(self, eventHandler):
        self.eventHandler = eventHandler
    
    def run(self):
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'secret!'
        self.socketio = SocketIO(app)
        self.socketio.on_namespace(self.eventHandler)
        self.socketio.run(app)
