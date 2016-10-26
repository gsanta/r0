from MotorMessage import MotorMessage

class MotorMessageSubscriber:

    def __init__(self, messagePublisher, messageProcessor):
        self.messagePublisher = messagePublisher
        self.messagePublisher.subscribe(self)
        self.messageProcessor = messageProcessor

    def notify(self):
        message = self.messagePublisher.getMessage()
        if message.category != 'motion':
            return
        
        motorMessage = MotorMessage(message.command)
        self.messageProcessor.process(motorMessage)