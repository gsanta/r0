from KineticStateTransition import KineticStateTransition
import time

class TimeBasedTurningTransition(KineticStateTransition):
    
    def __init__(self, kineticContext, terminalTime):
        KineticStateTransition.__init__(kineticContext)
        self.terminalState = kineticContext.getState()
        self.terminalTime = terminalTime
        
    def doTransition(self):
        
        if time.time() > self.terminalTime:
            self.kineticContext.setstate(self.kineticContext.getSate())
        else:
            self.kineticContext.setState(self.terminalState)
