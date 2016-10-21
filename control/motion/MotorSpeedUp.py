import time

class SpeedUpValues():
    def __init__(self, pwmValues, sleepTimes):
        self.pwmValues = pwmValues
        self.sleepTimes = sleepTimes

    def getPWMValues(self):
        return self.pwmValues

    def getSleepTimes(self):
        return self.sleepTimes

class MotorSpeedUp():
    def __init__(self, motorIO, speedUpValues, timer):
        self.motorIO = motorIO
        self.speedUpValues = speedUpValues
        self.timer = timer

    def speedUp(self):
        for i in range(0, len(self.speedUpValues.getPWMValues())):
            self.motorIO.changeSpeed(self.speedUpValues.getPWMValues()[i])
            self.timer.sleep(self.speedUpValues.getSleepTimes()[i])
	
