import unittest
from KineticCommand import KineticCommand
from KineticCommandState import KineticCommandState
class MotorControlStub:
    
    def __init__(self):
        self.val = None

    def forward(self):
        self.val = 'forward'

    def reverse(self):
        self.val = 'reverse'

    def turnLeft(self):
        self.val = 'turnLeft'

    def turnRight(self):
        self.val = 'turnRight'

    def stop(self):
        self.val = 'stop'

    def getVal(self):
        return self.val       

class KineticCommandSpec(unittest.TestCase):

    def testExecute(self):
        motorControl = MotorControlStub()
        command = KineticCommand(motorControl, KineticCommandState.FORWARD)
        command.execute()
        self.assertTrue(motorControl.getVal() == 'forward')

        command = KineticCommand(motorControl, KineticCommandState.REVERSE)
        command.execute()
        self.assertTrue(motorControl.getVal() == 'reverse')

        command = KineticCommand(motorControl, KineticCommandState.TURN_LEFT)
        command.execute()
        self.assertTrue(motorControl.getVal() == 'turnLeft')

        command = KineticCommand(motorControl, KineticCommandState.TURN_RIGHT)
        command.execute()
        self.assertTrue(motorControl.getVal() == 'turnRight')

        command = KineticCommand(motorControl, KineticCommandState.STOP)
        command.execute()
        self.assertTrue(motorControl.getVal() == 'stop')

if __name__ == '__main__':
    unittest.main()

