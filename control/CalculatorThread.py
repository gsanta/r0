import time
from threading import Thread

class CalculatorThread(Thread):

    def __init__(self, delay, initSensor, calcSensorData, addDataToSensor):
        Thread.__init__(self)
        self.initSensor = initSensor
        self.calcSensorData = calcSensorData
        self.addDataToSensor = addDataToSensor
        self.delay = delay

    def run(self):
        self.initSensor()

        while True:
            data = self.calcSensorData()
            self.addDataToSensor(data)
            time.sleep(self.delay)
