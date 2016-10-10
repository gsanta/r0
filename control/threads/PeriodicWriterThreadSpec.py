import unittest
from PeriodicWriterThread import PeriodicWriterThread

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

    def getAllData(self):
        return self.data

class RunOnThreadStub:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5]

    def runOnThread(self):
        return self.values.pop(0)

    def getData(self):
        return self.values

class TimerStub:

    def sleep(self, sleep):
        pass


class PeriodicWriterThreadSpec(unittest.TestCase):

    def testStart(self):
        createNewThread = CreateNewThreadStub(5)
        timer = TimerStub()
        inputDataProvider = InputDataProviderStub()
        runOnThread = RunOnThreadStub()

        periodicThread = PeriodicWriterThread(createNewThread.createNewThread, timer)
        periodicThread.start(inputDataProvider, runOnThread.runOnThread, 2, createNewThread.isFinished)
        self.assertTrue(inputDataProvider.getAllData() == [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()


