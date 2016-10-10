from PeriodicThread import PeriodicThread

class PeriodicWriterThread(PeriodicThread):

    def __init__(self, createNewThread, timer):
        PeriodicThread.__init__(self, createNewThread, timer)

    def _run(self):
        data = self.runOnThread()
        if data != None:
            self.inputDataProvider.addData(data)
