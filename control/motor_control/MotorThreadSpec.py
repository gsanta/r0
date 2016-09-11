import unittest
from MotorThread import MotorThread

class CreateThreadStub:

    def __init__(self):
        self.created = False

    def createNewThread(self, func):
        self.created = True

    def isCreated(self):
        return self.created

class TimerStub:
    def __init__(self):
        self.values = []

    def sleep(self, value):
        self.values.append(value)

    def getValues(self):
        return self.values

class InputDataProviderStub:

    def __init__(self, withData):
        self.data = None
        if withData == True:
            self.data = True

    def popData(self):
        return self.data

class WorkOnThreadStub:

    def __init__(self):
        self.data = False

    def runOnThread(self):
        self.data = True

    def getData(self):
        return self.data

class MotorThreadSpec(unittest.TestCase):

    def testThread(self):
        createThread = CreateThreadStub()
        timer = TimerStub()
        dataProvider = InputDataProviderStub(True)
        work = WorkOnThreadStub()

        thread = MotorThread(createThread.createNewThread, timer)
        thread.start(dataProvider, work, 2)

        self.assertTrue(createThread.isCreated() == True)

if __name__ == '__main__':
    unittest.main()

