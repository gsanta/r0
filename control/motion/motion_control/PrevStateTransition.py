from KineticStateTransition import KineticStateTransition
import time

class TimeBasedTurningTransition(KineticStateTransition):
    
    def __init__(self, kineticContext):
        KineticStateTransition.__init__(kineticContext)
        
    def doTransition(self):
        self.kineticContext.setState(self.terminalState)