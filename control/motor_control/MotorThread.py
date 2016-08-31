from ..sensor_consumer import LastSensorDataProvider
from ..threads import Timer
from threading import Thread

class MotorThread(Thread):

    def __init__(self, inputDataProvider, doWork, sleep):
        self.inputDataProvider = inputDataProvider
        self.doWork = doWork
        self.sleep = sleep

    def run(self):
        if self.inputDataProvider.popData != None:
            self.doWork()

        Timer.sleep(self.sleep)

