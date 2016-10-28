
class DistanceCalculator:
    speedOfSound = 34300

    def __init__(self, distanceSensorIO, timer):
        self.timer = timer
        self.distanceSensorIO = distanceSensorIO

    def initSensor(self):
        self.distanceSensorIO.triggerLow()

    def calcDistance(self):
        self.distanceSensorIO.triggerHigh()
        self.timer.sleep(0.00001)
        self.distanceSensorIO.triggerLow()

        pulseStart = self.distanceSensorIO.getPulseStart()
        pulseEnd = self.distanceSensorIO.getPulseEnd()

        distance = self.secondsToCentimeters(pulseEnd - pulseStart)
        
        return distance
    
    def secondsToCentimeters(self, elapsedTime):
        distance = elapsedTime * (DistanceCalculator.speedOfSound / 2)
        distance = round(distance, 2)
        return distance
