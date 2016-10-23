

class TaskRunner:
    """Prepares a task to be run on the async scheduler

    Args:
        scheduler (Scheduler)
        kineticContext (KineticContext)
    """
    def __init__(self, scheduler, kineticContext):
        self.scheduler = scheduler
        self.kineticContext = kineticContext

    def run(self):
        """Prepares and schedules a task
        """
        task = Task(self.kineticContext)
        scheduler.schedule(task)

class MotorDriver:
    """The entry point for driving the motor

    The motor runs automatically via state transitions after it is
    started with the `drive` method.
    Also with the `drive` method the state of the motor can be changed from outside

    Args:
        taskRunner (TaskRunner)
        kineticContext (KineticContext) 
    """    
    def __init__(self, taskRunner, kineticContext):
        self.taskRunner = taskRunner 
        self.kineticContext = kineticContext
    
    def drive(self, kineticState):
        """Sets the state of the motor
        
	Args:
            kineticState (KineticState)
        """
        self.kineticContext.setState(kineticState)
        self.taskRunner.run()

