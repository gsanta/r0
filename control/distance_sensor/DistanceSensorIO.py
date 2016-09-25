
class DistanceSensorIO:
    
    def __init__(self, trigPin, echoPin, gpioWrapper, resetTime, timer):
        self.trigPin = trigPin
        self.echoPin = echoPin
        self.gpioWrapper = gpioWrapper
        self.resetTime = resetTime
        self.timer = timer

    def setup(self):
        self.gpioWrapper.usePin(self.trigPin)
        self.gpioWrapper.usePin(self.echoPin)

    def triggerHigh(self):
        self.gpioWrapper.sendHigh(self.trigPin)

    def triggerLow(self):
        self.gpioWrapper.sendLow(self.trigPin)

    def isEchoHigh(self):
        return self.gpioWrapper.receive(self.echoPin) == True

    
    def getPulseStart(self):
        pulseStart = 0
        while self.isEchoHigh() == False:
            pulseStart = self.timer.time()
                            
        return pulseStart
                                
    def getPulseEnd(self):
        while self.isEchoHigh() == True:
            pulseEnd = self.timer.time()
        
        return pulseEnd

    def resetSensor(self):
        self.triggerHigh()
        self.timer.sleep(self.resetTime)
        self.triggerLow()

