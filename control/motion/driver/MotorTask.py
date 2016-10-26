

class MotorTask:

    def __init__(self, kineticContext, scheduler):
        self.kineticContext = kineticContext
        self.scheduler = scheduler
        self.aborted = False
        self.scheduler.schedule(self)

    def execute(self):
        self.kineticContext.move()
        
        if self.aborted == False:
            self.scheduler.schedule(self)
        
    def abort(self):
        self.aborted = True
        
    def isAborted(self):
        return self.aborted
