from KineticCommandState import KineticCommandState

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
