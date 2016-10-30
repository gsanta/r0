from flask_socketio import Namespace
import json

class SocketIOEventHandler(Namespace):
    
    def __init__(self, messagePublisher):
        Namespace.__init__(self, '')
        self.messagePublisher = messagePublisher
        
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_message(self, data):
        parsedData = json.loads(data)
        self.messagePublisher.dispatch(parsedData)