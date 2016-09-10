import RPi.GPIO as gpio
import time
import threading
import MotorThread
from MotorIO import MotorIO
from MotorIO import MotorPins

class MotorControl(object):

    def __init__(self, motorIO, sensorDataProvider, motorThread):
        self.pwm = None
        self.motorDataProvider = sensorDataProvider 
        self.motorThread = motorThread 
        self.motorIO = motorIO 
        self.motorThread.start()

    def forward(self):
        self.motorIO.forward()
        self.motorDataProvider.addData(True)
        print 'forward'

    def reverse(self):
        self.motorIO.reverse()
        self.motorDataProvider.addData(True)
        print 'reverse'
        

    def turn_left(self):
        self.motorIO.turn_left()
        self.motorDataProvider.addData(True)
        print 'turn_left'

    def turn_right(self):
        self.motorIO.turn_right()
        self.motorDataProvider.addData(True)
        print 'turn_right'

    def stop_motor(self):
        self.motorIO.stop_motor()
        self.motorDataProvider.addData(True)
        print 'stop_motor'

'''
class MotorControlAutomationWrapper(object):

    def __init__(self, motorControl, motorChannel):
        self.motorChannel = motorChannel
        self.thread = MotorControlAutomation(motorControl, motorChannel)

    
    def start(self):
        self.thread.start()

class MotorControlAutomation(threading.Thread):

    def __init__(self, motorControl, motorChannel):
        threading.Thread.__init__(self)
        self.motorControl = motorControl
        self.motorChannel = motorChannel
        
    
    def run(self):
        prevDirection = None
        direction = Direction.FORWARD

        while True:
            time.sleep(2)

            tmp = self.move(direction, prevDirection)
            prevDirection = direction
            direction = tmp

    def move(self, direction, prevDirection):
        if direction == prevDirection:
            return

        if direction == Direction.FORWARD:
            self.motorControl.forward()
            return Direction.FORWARD
        elif direction == Direction.REVERSE:
            self.motorControl.reverse()
            return Direction.REVERSE
        elif direction == Direction.LEFT:
            self.motorControl.turn_left()
            return Direction.LEFT
        elif direction == Direction.RIGHT:
            self.motorControl.turn_right()
            return Direction.RIGHT
        elif direction == Direction.STOP:
            self.motorControl.stop_motor()
            return Direction.STOP
'''
