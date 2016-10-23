from unittest.mock import patch
from unittest import TestCase
import unittest
from TimeBasedTransition import TimeBasedTransition

class KineticContextStub:

    def __init__(self):
        self.state = 'initialState'

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

class TimeBasedTransitionSpec(TestCase):
     
    @patch('time.time', return_value=2)
    def testDoTransitionBeforeTimeout(self, patchTime):
        kineticContext = KineticContextStub()
        terminalTime = 3
        terminalState = kineticContext.getState()
        transition = TimeBasedTransition(kineticContext, terminalTime)
       
        kineticContext.setState('anotherState')
       
        transition.doTransition()
        self.assertTrue(kineticContext.getState() == 'anotherState')
   
    @patch('time.time', return_value=2)
    def testDoTransitionAfterTimeout(self, patchTime):
        kineticContext = KineticContextStub()
        terminalTime = 1
        terminalState = kineticContext.getState()
        transition = TimeBasedTransition(kineticContext, terminalTime)
       
        kineticContext.setState('anotherState')
       
        transition.doTransition()
        self.assertTrue(kineticContext.getState() == terminalState)

if __name__ == '__main__':
    unittest.main()
