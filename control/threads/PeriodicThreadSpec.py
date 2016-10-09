import unittest
from PeriodicThread import PeriodicThread

class CreateNewThreadStub:
    
    def __init__(self, repeats):
        self.repeats = repeats


    def createNewThread(self, runOnThread):
        runOnThread()

    def isFinished(self):
        if self.repeats <= 0:
            return True

        self.repeats -= 1

        return False

class InputDataProviderStub:
    
    def __init__(self):
        self.data = []

    def addData(self, data):
        self.data.append(data)

    def getData(self):
        return self.data

class RunOnThreadStub:
    def __init__(self):
        self.counts = 0

    def runOnThread(self):
        actVal = self.counts
        self.counts += 1
        return actVal

class TimerStub:

    def sleep(self, sleep):
        pass


class PeriodicThreadImpl(PeriodicThread):
    def __init__(self, createNewThread, timer):
        PeriodicThread.__init__(self, createNewThread, timer)

    def _run(self):
        self.inputDataProvider.addData('newData')

class PeriodicThreadSpec(unittest.TestCase):

    def testStart(self):
        createNewThread = CreateNewThreadStub(5)
        timer = TimerStub()
        inputDataProvider = InputDataProviderStub()
        runOnThread = RunOnThreadStub()

        periodicThread = PeriodicThreadImpl(createNewThread.createNewThread, timer)
        periodicThread.start(inputDataProvider, runOnThread, 2, createNewThread.isFinished)
        self.assertTrue(len(inputDataProvider.getData()) == 5)
        self.assertTrue(inputDataProvider.getData()[-1] == 'newData')

if __name__ == '__main__':
    unittest.main()


