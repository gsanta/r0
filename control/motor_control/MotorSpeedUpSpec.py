import unittest
from MotorSpeedUp import MotorSpeedUp
from MotorSpeedUp import SpeedUpValues

class MotorIOStub:
    
    def __init__(self):
        self.speedValues = []    

    def changeSpeed(self, speed):
        self.speedValues.append(speed)

    def getSpeedValues(self):
        return self.speedValues

class TimerStub:
    def __init__(self):
        self.timerValues = []

    def sleep(self, sleepValue):
        self.timerValues.append(sleepValue)

    def getTimerValues(self):
        return self.timerValues

class MotorSpeedUpSpec(unittest.TestCase):

    def testSpeedValues(self):
        speedUpValues = SpeedUpValues([1,2,3], [2,2,4])
        timer = TimerStub()
        motorIO = MotorIOStub()
        motorSpeedUp = MotorSpeedUp(motorIO, speedUpValues, timer)
        motorSpeedUp.speedUp()

        timerValues = timer.getTimerValues()
        speedValues = motorIO.getSpeedValues()
        self.assertTrue(timerValues[0] == 2)

if __name__ == '__main__':
    unittest.main()

