
class MotorControl(object):

    def __init__(self, motorIO):
        self.motorIO = motorIO 

    def forward(self):
        self.motorIO.forward()

    def reverse(self):
        self.motorIO.reverse()

    def turnLeft(self):
        self.motorIO.turnLeft()

    def turnRight(self):
        self.motorIO.turnRight()

    def stopMotor(self):
        self.motorIO.stopMotor()

