from enum import Enum

class KineticCommandState(Enum):
        FORWARD = 1,
        REVERSE = 2,
        TURN_LEFT = 3,
        TURN_RIGHT = 4,
        STOP = 5


class KineticCommand():
    
    def __init__(self, motorControl, kineticCommandState):
        self.motorControl = motorControl
        self.kineticCommandState = kineticCommandState
    
    def execute(self):
        if self.kineticCommandState == KineticCommandState.FORWARD:
            self.motorControl.forward()
        elif self.kineticCommandState == KineticCommandState.REVERSE:
            self.motorControl.reverse()
        elif self.kineticCommandState == KineticCommandState.TURN_LEFT:
            self.motorControl.turnLeft()
        elif self.kineticCommandState == KineticCommandState.TURN_RIGHT:
            self.motorControl.turnRight()
        else:
            self.motorControl.stop()