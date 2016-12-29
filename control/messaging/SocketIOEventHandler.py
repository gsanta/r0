from flask_socketio import Namespace
from kafka import SimpleProducer, KafkaClient
import json

class SocketIOEventHandler(Namespace):
    
    def __init__(self, messagePublisher):
        Namespace.__init__(self, '')
        self.messagePublisher = messagePublisher
#         kafkaClient = KafkaClient('localhost:9092')
#         self.kafkaProducer = SimpleProducer(kafkaClient)
        
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_message(self, data):
        pass
#         producer.send_messages(topic, b'abcd')
#         byteData = str.encode(json.dumps(data))
#         self.kafkaProducer.send_messages('test', byteData)
#         self.messagePublisher.dispatch(data)
#         print(
#             str.encode(
#                 json.dumps(data)
#             )
#         )
#         parsedData = json.loads(data)
#         self.messagePublisher.dispatch(parsedData)
