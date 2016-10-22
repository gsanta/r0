

class MotorMessageSubscriber:

    def __init__(self, messagePublisher):
        self.messagePublisher = messagePublisher
        self.messagePublisher.subscribe(self)

    def notify(self):
        message = self.messagePublisher.getMessage()
        
