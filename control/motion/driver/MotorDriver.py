from .MotorTask import MotorTask

class MotorDriver:
    """The entry point for driving the motor

    The motor runs automatically via state transitions after it is
    started with the `drive` method.
    Also with the `drive` method the state of the motor can be changed from outside

    Args:
        kineticContext (KineticContext) 
    """    
    def __init__(self, kineticContext, scheduler):
        self.kineticContext = kineticContext
        self.scheduler = scheduler
        self.currentTask = None
    
    def drive(self, kineticState):
        """Sets the state of the motor
        
	    Args:
            kineticState (KineticState)
        """
        if self.currentTask != None:
            self.currentTask.abort()
        
        self.kineticContext.setState(kineticState)
        self.currentTask = MotorTask(self.kineticContext, self.scheduler)