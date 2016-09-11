import unittest
from MotorControl import MotorControl

class MotorIOStub:
    
    def __init__(self):
        self.values = []


    def forward(self):
        self.values.append('forward')

    def reverse(self):
        self.values.append('reverse')

    def turnRight(self):
        self.values.append('turnRight')

    def turnLeft(self):
        self.values.append('turnLeft')

    def stopMotor(self):
        self.values.append('stopMotor')

    def getValues(self):
        return self.values

class SensorDataProviderStub:

    def __init__(self):
        self.values = []

    def addData(self, data):
        self.values.append(data)

    def getValues(self):
        return self.values

class MotorThreadStub:

    def start(self):
        pass

class MotorControlSpec(unittest.TestCase):

    def testForward(self):
        motorIO = MotorIOStub()
        dataProvider = SensorDataProviderStub()
        motorControl = MotorControl(motorIO, dataProvider, MotorThreadStub())

        motorControl.forward()
        self.assertTrue(motorIO.getValues()[0] == 'forward')
        self.assertTrue(dataProvider.getValues()[0] == True)

    def testReverse(self):
        motorIO = MotorIOStub()
        dataProvider = SensorDataProviderStub()
        motorControl = MotorControl(motorIO, dataProvider, MotorThreadStub())

        motorControl.reverse()
        self.assertTrue(motorIO.getValues()[0] == 'reverse')
        self.assertTrue(dataProvider.getValues()[0] == True)

    def testTurnLeft(self):
        motorIO = MotorIOStub()
        dataProvider = SensorDataProviderStub()
        motorControl = MotorControl(motorIO, dataProvider, MotorThreadStub())

        motorControl.turnLeft()
        self.assertTrue(motorIO.getValues()[0] == 'turnLeft')
        self.assertTrue(dataProvider.getValues()[0] == True)
    
    def testTurnRight(self):
        motorIO = MotorIOStub()
        dataProvider = SensorDataProviderStub()
        motorControl = MotorControl(motorIO, dataProvider, MotorThreadStub())

        motorControl.turnRight()
        self.assertTrue(motorIO.getValues()[0] == 'turnRight')
        self.assertTrue(dataProvider.getValues()[0] == True)
    
    def testStopMotor(self):
        motorIO = MotorIOStub()
        dataProvider = SensorDataProviderStub()
        motorControl = MotorControl(motorIO, dataProvider, MotorThreadStub())

        motorControl.stopMotor()
        self.assertTrue(motorIO.getValues()[0] == 'stopMotor')
        self.assertTrue(dataProvider.getValues()[0] == True)

if __name__ == '__main__':
    unittest.main()



