from KineticStateTransition import KineticStateTransition
import time

class TimeBasedTransition(KineticStateTransition):
    
    def __init__(self, kineticContext, terminalTime):
        KineticStateTransition.__init__(self, kineticContext)
        self.terminalState = kineticContext.getState()
        self.terminalTime = terminalTime
        
    def doTransition(self):
        
        if time.time() > self.terminalTime:
            self.kineticContext.setState(self.terminalState)
