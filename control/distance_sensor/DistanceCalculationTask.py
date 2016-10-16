

class DistanceCalculationTask
    
    def __init__(self, distanceCalculator, resultHandler):
        self.calculator = distanceCalculator

    def execute(self):
        return self.calculator.calcDistance()

    def setResult(self, result):
        resultHandler.setResult(result)

