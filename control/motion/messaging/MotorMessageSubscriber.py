from .MotorMessage import MotorMessage

class MotorMessageSubscriber:

    def __init__(self, messagePublisher, messageProcessor):
        self.messagePublisher = messagePublisher
        self.messagePublisher.register(self)
        self.messageProcessor = messageProcessor

    def notify(self):
        message = self.messagePublisher.getMessage()
        if message['category'] != 'MOTION':
            return
        
        motorMessage = MotorMessage(message['command'])
        self.messageProcessor.process(motorMessage)
