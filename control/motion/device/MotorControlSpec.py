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

class MotorControlSpec(unittest.TestCase):

    def testForward(self):
        motorIO = MotorIOStub()
        motorControl = MotorControl(motorIO)

        motorControl.forward()
        self.assertTrue(motorIO.getValues()[0] == 'forward')

    def testReverse(self):
        motorIO = MotorIOStub()
        motorControl = MotorControl(motorIO)

        motorControl.reverse()
        self.assertTrue(motorIO.getValues()[0] == 'reverse')

    def testTurnLeft(self):
        motorIO = MotorIOStub()
        motorControl = MotorControl(motorIO)

        motorControl.turnLeft()
        self.assertTrue(motorIO.getValues()[0] == 'turnLeft')
    
    def testTurnRight(self):
        motorIO = MotorIOStub()
        motorControl = MotorControl(motorIO)

        motorControl.turnRight()
        self.assertTrue(motorIO.getValues()[0] == 'turnRight')
    
    def testStopMotor(self):
        motorIO = MotorIOStub()
        motorControl = MotorControl(motorIO)

        motorControl.stopMotor()
        self.assertTrue(motorIO.getValues()[0] == 'stopMotor')

if __name__ == '__main__':
    unittest.main()



