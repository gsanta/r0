

class MotorMessageProcessor:

    def __init__(self, motorDriver, kineticStateFactory):
        self.motorDriver = motorDriver
        self.kineticStateFactory = kineticStateFactory

    def process(self, message):
        kineticState = self.kineticStateFactory.getKineticState(message.getCommand())
        self.motorDriver.drive(kineticState)
