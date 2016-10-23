
class MotorMessage:

    def __init__(self, command):
        self.command = command

    def getCommand(self):
        return self.command

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
