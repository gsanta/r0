


class KineticStateFactory:

    def __init__(self, motorControl):
        self.motorControl = motorControl

    def getForwardMotionState(self, kineticContext):
        kineticCommand = KineticCommand(self.motorControl, KineticCommandState.FORWARD)
        kineticStateTransition = PrevStateTransition(kineticContext)
        return KineticState(kineticCommand, kineticStateTransition)

    def getReverseMotionState(self, kineticContext):
        kineticCommand = KineticCommand(self.motorControl, KineticCommandState.REVERSE)
        kineticStateTransition = PrevStateTransition(kineticContext)
        return KineticState(kineticCommand, kineticStateTransition)
    
    def getTurnLeftMotionState(self, kineticContext):
        kineticCommand = KineticCommand(self.motorControl, KineticCommandState.TURN_LEFT)
        endTime = time.time() + 2
        kineticStateTransition = TimeBasedTurningTransition(kineticContext, endTime)
        return KineticState(kineticCommand, kineticStateTransition)

    def getTurnRightMotionState(self, kineticContext):
        kineticCommand = KineticCommand(self.motorControl, KineticCommandState.TURN_RIGHT)
        endTime = time.time() + 2
        kineticStateTransition = TimeBasedTurningTransition(kineticContext, endTime)
        return KineticState(kineticCommand, kineticStateTransition)

    def getStopMotionState(self, kineticContext):
        kineticCommand = KineticCommand(self.motorControl, KineticCommandState.STOP)
        kineticStateTransition = PrevStateTransition(kineticContext)
        return KineticState(kineticCommand, kineticStateTransition)
        
