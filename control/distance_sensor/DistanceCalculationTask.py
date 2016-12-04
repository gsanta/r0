

class DistanceCalculationTask:
    
    def __init__(self, distanceCalculator, resultHandler, scheduler):
        self.calculator = distanceCalculator
        self.scheduler = scheduler
        self.aborted = False
        self.scheduler.schedule(self)

    def execute(self):
        distance = self.calculator.calcDistance()
        self.resultHandler.setData(distance)
        
        if self.aborted == False:
            self.scheduler.schedule(self)
        
    def abort(self):
        self.aborted = True
        
    def isAborted(self):
        return self.aborted
