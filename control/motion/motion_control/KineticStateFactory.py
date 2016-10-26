from KineticCommand import KineticCommand
from KineticCommandState import KineticCommandState
from NoopTransition import NoopTransition
from TimeBasedTransition import TimeBasedTransition

class KineticStateFactory:

    def __init__(self, motorControl, kineticContext):
        self.motorControl = motorControl
        self.kineticContext = kineticContext

    def getKineticState(self, kineticCommandState):
        kineticCommand = KineticCommand(self.motorControl, kineticCommandState)
        kineticStateTransition = self._getKineticStateTransition(kineticCommandState)
        return KineticState(kineticCommand, kineticStateTransition)

    def _getKineticStateTransition(kineticCommandState):
        if kineticCommandState == KineticCommandState.FORWARD or kineticCommandState == KineticCommandState.REVERSE:
            return NoopTransition(self.kineticContext)
        else:
            endTime = time.time() + 2
            return TimeBasedTransition(self.kineticContext, endTime)
