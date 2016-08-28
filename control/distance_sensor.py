import RPi.GPIO as GPIO
import time
from threading import Thread
import Queue


class DistanceSensor(object):

    def __init__(self, trigPin, echoPin, dataProvider, threadFactory):
        self.trigPin = trigPin
        self.echoPin = echoPin
        self.dataProvider = dataProvider
        self.thread = threadFactory.getCalculatorThread(self._initSensor, self._calcDistance, self._addDistance)
        self._setup()

    def _setup(self):
        GPIO.setup(self.trigPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
    
    def _initSensor(self):
        GPIO.output(self.trigPin, False)
        print "Waiting For Sensor To Settle"
        time.sleep(2)

    def _calcDistance(self):
        GPIO.output(self.trigPin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigPin, False)

        while GPIO.input(self.echoPin) == 0:
            pulseStart = time.time()

        while GPIO.input(self.echoPin) == 1:
            pulseEnd = time.time()

        pulseDuration = pulseEnd - pulseStart
        distance = pulseDuration * 17150
        distance = round(distance, 2)
        
        return distance;

    def _addDistance(self, distance):
        dataProvider.addData(distance)

    def startSensor(self):
        self.thread.start()
