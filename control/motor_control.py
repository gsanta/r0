import RPi.GPIO as gpio
import time

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

    def __init__(self, motorPins):
        self.pwm = None
        self.motorPins = motorPins
        self._init()

    def _init(self):
        gpio.setmode(gpio.BOARD)
       # gpio.setup(32, gpio.OUT)
        print self.motorPins.getPWM() 
        gpio.setup(self.motorPins.getPWM(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightReverse(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftReverse(), gpio.OUT)
        self.pwm = gpio.PWM(self.motorPins.getPWM(), 50)
        self.pwm.start(50)

    def forward(self):
        gpio.output(self.motorPins.getMotorRightReverse(), False)
        gpio.output(self.motorPins.getMotorRightForward(), True)
        gpio.output(self.motorPins.getMotorLeftForward(), True)
        gpio.output(self.motorPins.getMotorLeftReverse(), False)

    def reverse(self):
        gpio.output(self.motorPins.getMotorRightReverse(), True)
        gpio.output(self.motorPins.getMotorRightForward(), False)
        gpio.output(self.motorPins.getMotorLeftForward(), False)
        gpio.output(self.motorPins.getMotorLeftReverse(), True)

    def turn_left(self):
        gpio.output(self.motorPins.getMotorRightReverse(), True)
        gpio.output(self.motorPins.getMotorRightForward(), False)
        gpio.output(self.motorPins.getMotorLeftForward(), False)
        gpio.output(self.motorPins.getMotorLeftReverse(), False)

    def turn_right(self):
        gpio.output(self.motorPins.getMotorRightReverse(), False)
        gpio.output(self.motorPins.getMotorRightForward(), False)
        gpio.output(self.motorPins.getMotorLeftForward(), False)
        gpio.output(self.motorPins.getMotorLeftReverse(), True)

    def stop_motor(self):
        gpio.output(self.motorPins.getMotorRightReverse(), False)
        gpio.output(self.motorPins.getMotorRightForward(), False)
        gpio.output(self.motorPins.getMotorLeftForward(), False)
        gpio.output(self.motorPins.getMotorLeftReverse(), False)

