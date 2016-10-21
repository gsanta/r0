from KineticStateTransition import KineticStateTransition
import time

class TimeBasedTurningTransition(KineticStateTransition):
    
    def __init__(self, kineticContext, terminalState, terminalTime):
        KineticStateTransition.__init__(kineticContext)
        self.terminalState = terminalState
        self.terminalTime = terminalTime
        
    def doTransition(self):
        
        if time.time() > self.terminalTime:
            self.kineticContext.setstate(self.kineticContext.getSate())
        else:
            self.kineticContext.setState(self.terminalState)