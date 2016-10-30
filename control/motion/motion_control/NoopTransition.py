from ..motion_control.KineticStateTransition import KineticStateTransition
import time

class NoopTransition(KineticStateTransition):
    
    def __init__(self, kineticContext):
        KineticStateTransition.__init__(kineticContext)
        
    def doTransition(self):
        pass
