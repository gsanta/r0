import RPi.GPIO as GPIO
from threading import Thread
from ..threads import Timer
import Queue


class DistanceSensor(object):

    def __init__(self, distanceSensorIO, dataProvider, threadFactory, timer):
        self.timer = timer
        self.dataProvider = dataProvider
        self.thread = threadFactory.getCalculatorThread(self._initSensor, self._calcDistance, self._addDistance)
        self.distanceSensorIO = distanceSensorIO
        self.distanceSensorIO.setup()

    def _initSensor(self):
        self.distanceSensorIO.triggerLow()

    def _calcDistance(self):
        self.distanceSensorIO.triggerHigh()
        timer.sleep(0.00001)
        self.distanceSensorIO.triggerLow()

        while self.distanceSensorIO.isEchoHigh() == False:  
            pulseStart = time.time()

        while self.distanceSensorIO.isEchoHigh() == True:
            pulseEnd = time.time()

        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150
        distance = round(distance, 2)
        
        return distance;

    def _addDistance(self, distance):
        self.dataProvider.addData(distance)

    def startSensor(self):
        self.thread.start()
