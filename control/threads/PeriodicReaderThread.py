from PeriodicThread import PeriodicThread

class PeriodicReaderThread(PeriodicThread):

    def __init__(self, createNewThread, timer):
        PeriodicThread.__init__(self, createNewThread, timer)

    def _run(self):
        data = self.inputDataProvider.getData()
        if data != None:
            self.runOnThread(data)
