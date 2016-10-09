import abc

def alwaysFalse():
    return False

class PeriodicThread(metaclass = abc.ABCMeta):
    """Abstract class for periodically run a task on a separate thread"""

    def __init__(self, createNewThread, timer):
        """
        Args:
            createNewThread (function): accepts a function, representing the work to do and runs
                that work periodiccaly on a new thread.
            timer (Timer): -
        """

        self.createNewThread = createNewThread
        self.timer = timer

    def start(self, inputDataProvider, runOnThread, sleep, isFinished = alwaysFalse):
        """ Starts the thread

        Args: 
            inputDataProvider (DataProvider): The result after each period is added/read to/from it
            runOnThread (function): The actual work that should be run on the thread
            sleep (number): the number of seconds to sleep after each period
        """
        self.inputDataProvider = inputDataProvider
        self.runOnThread = runOnThread
        self.sleep = sleep
        self.isFinished = isFinished
        self.createNewThread(self._runPeriodically)
    
    def _runPeriodically(self):
        while not self.isFinished():
            self._run()

        self.timer.sleep(self.sleep)

    @abc.abstractmethod
    def _run(self):
        pass

