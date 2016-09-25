import RPi.GPIO as GPIO
from threading import Thread
from ..threads import Timer
import Queue

class DistanceCalculator:
    
    def __init__(self, distanceSensorIO, dataProvider, timer):
        self.distanceSensorIO = distanceSensorIO
        self.dataProvider = dataProvider
        self.timer = timer

    def initSensor(self):
        self.distanceSensorIO.triggerLow()

    def calcDistance(self):
        self.distanceSensorIO.triggerHigh()
        timer.sleep(0.00001)
        self.distanceSensorIO.triggerLow()

        while self.distanceSensorIO.isEchoHigh() == False:  
            pulseStart = timer.time()

        while self.distanceSensorIO.isEchoHigh() == True:
            pulseEnd = timer.time()

        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150
        distance = round(distance, 2)
        
        self.dataProvider.addData(distance);

