
class MotorControl(object):

    def __init__(self, motorIO, sensorDataProvider, motorThread):
        self.motorDataProvider = sensorDataProvider 
        self.motorThread = motorThread 
        self.motorIO = motorIO 
        self.motorThread.start()

    def forward(self):
        self.motorIO.forward()
        self.motorDataProvider.addData(True)

    def reverse(self):
        self.motorIO.reverse()
        self.motorDataProvider.addData(True)

    def turnLeft(self):
        self.motorIO.turnLeft()
        self.motorDataProvider.addData(True)

    def turnRight(self):
        self.motorIO.turnRight()
        self.motorDataProvider.addData(True)

    def stopMotor(self):
        self.motorIO.stopMotor()
        self.motorDataProvider.addData(True)

