
class MotorControl(object):

    def __init__(self, motorIO, sensorDataProvider):
        self.motorDataProvider = sensorDataProvider 
        self.motorIO = motorIO 

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

