import unittest
from PeriodicReaderThread import PeriodicReaderThread

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
        self.data = [1, 2, 3, 4, 5]


    def getData(self):
        return self.data.pop(0)

class RunOnThreadStub:
    def __init__(self):
        self.values = []

    def runOnThread(self, data):
        self.values.append(data)

    def getData(self):
        return self.values

class TimerStub:

    def sleep(self, sleep):
        pass


class PeriodicReaderThreadSpec(unittest.TestCase):

    def testStart(self):
        createNewThread = CreateNewThreadStub(5)
        timer = TimerStub()
        inputDataProvider = InputDataProviderStub()
        runOnThread = RunOnThreadStub()

        periodicThread = PeriodicReaderThread(createNewThread.createNewThread, timer)
        periodicThread.start(inputDataProvider, runOnThread.runOnThread, 2, createNewThread.isFinished)
        self.assertTrue(runOnThread.getData() == [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()


