class KineticStateFactory:

    def __init__(self, motorControl, kineticContext):
        self.motorControl = motorControl
        self.kineticContext = kineticContext

    def getKineticState(self, kineticCommandState):
        kineticCommand = KineticCommand(self.motorControl, kineticCommandState)
        kineticStateTransition = self._getKineticStateTransition(kineticCommandState)
        return KineticState(kineticCommand, kineticStateTransition)

    def _getKineticStateTransition(kineticCommandState)
        if kineticCommandState == KineticCommandState.FORWARD or
            kineticCommandState == KineticCommandState.REVERSE:
            return PrevStateTransition(self.kineticContext)
        else:
            endTime = time.time() + 2
            return TimeBasedTurningTransition(self.kineticContext, endTime)
