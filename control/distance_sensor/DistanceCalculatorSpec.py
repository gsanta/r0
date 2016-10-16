import unittest
from DistanceCalculator import DistanceCalculator

class DistanceSensorIOStub:

    def __init__(self, pulseStart, pulseEnd):
        self.pulseStart = pulseStart
        self.pulseEnd = pulseEnd

    def triggerHigh(self):
        pass

    def triggerLow(self):
        pass

    def getPulseStart(self):
        return self.pulseStart

    def getPulseEnd(self):
        return self.pulseEnd


class TimerStub:

    def sleep(self, sleep):
        pass

class DistanceCalculatorSpec(unittest.TestCase):

    def testSecondsToCentimeters(self):
        distanceCalculator = DistanceCalculator(None, None)

        dist = distanceCalculator.secondsToCentimeters(5)
        self.assertTrue(dist == 85750)

    def testCalcDistance(self):
        distanceSensorIO = DistanceSensorIOStub(5, 8)
        timer = TimerStub()

        distanceCalculator = DistanceCalculator(distanceSensorIO, timer)
        dist = distanceCalculator.calcDistance()
        print(dist)
        self.assertTrue(dist == 51450)


if __name__ == '__main__':
    unittest.main()



    
