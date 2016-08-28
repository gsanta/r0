
import unittest
from DistanceSensorIO import DistanceSensorIO 

class GPIOWrapperStub:

    def __init__(self):
        self.pins = {}
    
    def usePin(self, pinNum):
        self.pins[pinNum] = False

    def sendHigh(self, pinNum):
        self.pins[pinNum] = True

    def sendLow(self, pinNum):
        self.pins[pinNum] = False

    def receive(self, pinNum):
        return self.pins.get(pinNum)
    
    def isUsed(self, pinNum):
        print(self.pins[pinNum])

class DistanceSensorIOSpec(unittest.TestCase):

    def testSetup(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub)
        io.setup()
        self.assertTrue(stub.pins.get(1) == False)
        self.assertTrue(stub.pins.get(2) == False)

    def testTriggerHigh(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub)
        io.triggerHigh()
        self.assertTrue(stub.pins.get(1) == True)

    def testTriggerLow(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub)
        io.triggerHigh()
        io.triggerLow()
        self.assertTrue(stub.pins.get(1) == False)

    def testIsEchoHigh(self):
        stub = GPIOWrapperStub()
        io = DistanceSensorIO(1, 2, stub)
        self.assertTrue(io.isEchoHigh() == False)

if __name__ == '__main__':
    unittest.main()
