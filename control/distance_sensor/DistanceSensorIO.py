
class DistanceSensorIO:
    
    def __init__(self, trigPin, echoPin, gpioWrapper):
        self.trigPin = trigPin
        self.echoPin = echoPin
        self.gpioWrapper = gpioWrapper

    def setup(self):
        self.gpioWrapper.usePin(self.trigPin)
        self.gpioWrapper.usePin(self.echoPin)

    def triggerHigh(self):
        self.gpioWrapper.sendHigh(self.trigPin)

    def triggerLow(self):
        self.gpioWrapper.sendLow(self.trigPin)

    def isEchoHigh(self):
        return self.gpioWrapper.receive(self.echoPin) == True
