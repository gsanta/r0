import zerorpc
import json

class MessageHook:

    def __init__(self, messagePublisher):
        self.messagePublisher = messagePublisher
    
    def receive(self, message):
	message = json.loads(message)
        self.messagePublisher.publish(message)

class RPCBridge:

    def __init__(self, address, hook):
        self.address = address
        self.hook = hook

    def run(self):
        server = zerorpc.Server(self.hook)
        server.bind(self.address)
        server.run()
