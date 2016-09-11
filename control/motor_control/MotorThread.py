
class MotorThread:
    def __init__(self, createNewThread, timer):
        self.createNewThread = createNewThread
        self.timer = timer
        
    def start(self, inputDataProvider, runOnThread, sleep):
        self.inputDataProvider = inputDataProvider
        self.runOnThread = runOnThread
        self.sleep = sleep

        self.createNewThread(self._run)

    def _run(self):
        if self.inputDataProvider.popData() != None:
            self.doWork()

        self.timer(self.sleep)

