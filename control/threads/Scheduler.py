


class TaskRunner:
    
    def __init__(self, asyncScheduler, blockingScheduler):
        self.asyncScheduler = asyncScheduler
        self.blockingScheduler = blockingScheduler
        
    
    def scheduleWith(self, task, scheduler):
        runner.schedule(task)
        