import RPi.GPIO as gpio
import time
import threading

class Direction:
    FORWARD = 0
    RIGHT = 1
    REVERSE = 2
    LEFT = 3
    STOP = 4



class MotorPins(object):

    def __init__(self):
        self.pwm = None

    def setPWM(self, pwm):
        self.pwm = pwm

    def getPWM(self):
        return self.pwm

    def setMotorRightForward(self, mrf):
        self.mrf = mrf

    def getMotorRightForward(self):
        return self.mrf

    def setMotorRightReverse(self, mrr):
        self.mrr = mrr

    def getMotorRightReverse(self):
        return self.mrr

    def setMotorLeftForward(self, mlf):
        self.mlf = mlf

    def getMotorLeftForward(self):
        return self.mlf

    def setMotorLeftReverse( self, mlr):
        self.mlr = mlr

    def getMotorLeftReverse(self):
        return self.mlr

class MotorControl(object):

    def __init__(self, motorPins, pwmValues, pwmTimers):
        self.pwm = None
        self.motorPins = motorPins
        self.pwmValues = pwmValues
        self.pwmTimers = pwmTimers
        self._init()

    def _init(self):
        gpio.setmode(gpio.BOARD)
       # gpio.setup(32, gpio.OUT)
        gpio.setup(self.motorPins.getPWM(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightReverse(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftReverse(), gpio.OUT)
        self.pwm = gpio.PWM(self.motorPins.getPWM(), 50)
        self.pwm.start(self.pwmValues[0])

    def start(self):
        for i in range(0, len(self.pwmValues)):
            print self.pwmValues[i]

            self.pwm.ChangeDutyCycle(self.pwmValues[i])
            time.sleep(self.pwmTimers[i])
    
    def forward(self):
        self.setupPins(True, False, True, False)
        self.t = threading.Thread(target=self.start)
        self.t.start()
        print 'forward'
        #self.start()

    def reverse(self):
        self.setupPins(False, True, False, True)
        self.t = threading.Thread(target=self.start)
        self.t.start()
        print 'reverse'

    def turn_left(self):
        self.setupPins(False, True, False, False)
        self.t = threading.Thread(target=self.start)
        self.t.start()
        print 'turn_left'

    def turn_right(self):
        self.setupPins(False, False, False, True)
        self.t = threading.Thread(target=self.start)
        self.t.start()
        print 'turn_right'

    def stop_motor(self):
        self.setupPins(False, False, False, False)
        print 'stop_motor'

    def setupPins(self, mrf, mrr, mlf, mlr):
        gpio.output(self.motorPins.getMotorRightReverse(), mrr)
        gpio.output(self.motorPins.getMotorRightForward(), mrf)
        gpio.output(self.motorPins.getMotorLeftForward(), mlf)
        gpio.output(self.motorPins.getMotorLeftReverse(), mlr)

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
