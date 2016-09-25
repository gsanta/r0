
import unittest
from DistanceSensorIO import DistanceSensorIO 

class GPIOWrapperStub:

    def __init__(self, toggleCounter = 0):
        self.pins = {}
        self.toggleCounter = toggleCounter
    
    def usePin(self, pinNum):
        self.pins[pinNum] = False

    def sendHigh(self, pinNum):
        self.pins[pinNum] = True

    def sendLow(self, pinNum):
        self.pins[pinNum] = False

    def receive(self, pinNum):
        if self.toggleCounter == 0:
            return self.pins.get(pinNum)
        else:
            self.toggleCounter = self.toggleCounter - 1
            return not self.pins.get(pinNum)
    
    def isUsed(self, pinNum):
        print(self.pins[pinNum])

class TimerStub:
    def __init__(self):
        self.currentTime = 0
        self.sleeps = []

    def time(self):
        actTime = self.currentTime
        self.currentTime = self.currentTime + 1
        return actTime

    def sleep(self, seconds):
        self.sleeps.append(seconds)

    def getSleepValues(self):
        return self.sleeps


class DistanceSensorIOSpec(unittest.TestCase):

    def testSetup(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub, None, 0)
        io.setup()
        self.assertTrue(stub.pins.get(1) == False)
        self.assertTrue(stub.pins.get(2) == False)

    def testTriggerHigh(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub, None, 0)
        io.triggerHigh()
        self.assertTrue(stub.pins.get(1) == True)

    def testTriggerLow(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub, None, 0)
        io.triggerHigh()
        io.triggerLow()
        self.assertTrue(stub.pins.get(1) == False)

    def testIsEchoHigh(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub, None, 0)
        self.assertTrue(io.isEchoHigh() == False)

    def testGetPulseStart(self):
        stub = GPIOWrapperStub(5)
        timer = TimerStub()
        io = DistanceSensorIO(1, 2, stub, timer, 0)
        io.triggerHigh()
        pulseStart = io.getPulseStart()
        print(pulseStart)
        self.assertTrue(pulseStart == 6)


if __name__ == '__main__':
    unittest.main()
