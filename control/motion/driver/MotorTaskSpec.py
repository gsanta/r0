import unittest
from MotorTask import MotorTask

class SchedulerStub:
    
    def __init__(self):
        self.counter = 4
    
    def schedule(self, task):
        self.counter -= 1
        
        if self.counter == 0:
            task.abort()
        else:
            task.execute()
            
class KineticContextStub:
    
    def __init__(self):
        self.counter = 0
        
    def move(self):
        self.counter += 1
        
    def getCount(self):
        return self.counter

class MotorTaskSpec(unittest.TestCase):
    
    def testTaskScheduling(self):
        scheduler = SchedulerStub()
        kineticContext = KineticContextStub()
        
        motorTask = MotorTask(kineticContext, scheduler)
        print(kineticContext.getCount())
        self.assertTrue(kineticContext.getCount() == 3)
        
        
if __name__ == '__main__':
    unittest.main()