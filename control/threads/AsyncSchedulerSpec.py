import unittest
from AsyncTaskRunner import AsyncTaskRunner

class TaskStub:
    
    def __init__(self):
        self.values = []

    def execute(self):
        print('execute run')
        self.values.append(len(values) + 1)

    def getValues(self):
        return self.values

class AsyncIOStub:

    def __init__(self):
        self.sleeps = []

    def ensure_future(self, future):
        pass

    def sleep(self, val):
        self.sleeps.append(val)

    def getSleeps():
        return self.sleeps

class AsyncSchdeulerSpec(unittest.TestCase):

    def testSchedule(self):
        asyncTaskRunner = AsyncTaskRunner(AsyncIOStub())
        task = TaskStub()
        asyncTaskRunner.run(task, 2)
        print(task.getValues())
        self.assertTrue(task.getValues() == [1])

if __name__ == '__main__':
    unittest.main()

