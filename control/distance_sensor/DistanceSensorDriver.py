

class DistanceSensorDriver:
    
    def __init__(self, distanceCalculator, scheduler):
        self.scheduler = scheduler
        self.distanceCalculator = distanceCalculator