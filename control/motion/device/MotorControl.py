
class MotorControl(object):

    def __init__(self, motorIO):
        self.motorIO = motorIO 

    def forward(self):
        print('forward')
        self.motorIO.forward()

    def reverse(self):
        print('reverse')
        self.motorIO.reverse()

    def turnLeft(self):
        print('turn_left')
        self.motorIO.turnLeft()

    def turnRight(self):
        print('turn_right')
        self.motorIO.turnRight()

    def stopMotor(self):
        print('stop')
        self.motorIO.stopMotor()

