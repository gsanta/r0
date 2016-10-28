

class DistanceCalculationTask:
    
    def __init__(self, distanceCalculator, resultHandler):
        self.calculator = distanceCalculator

    def execute(self):
        distance = self.calculator.calcDistance()
        self.resultHandler.setResult(distance)
