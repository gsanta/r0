
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


class MotorIO:

    def __init__(self, motorPins):
        self.motorPins = motorPins

    def setup(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.motorPins.getPWM(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightReverse(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorRightForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftForward(), gpio.OUT)
        gpio.setup(self.motorPins.getMotorLeftReverse(), gpio.OUT)
        self.pwm = gpio.PWM(self.motorPins.getPWM(), 50)
        self.pwm.start(self.pwmValues[0])


    def forward(self):
        self.setupPins(True, False, True, False)

    def reverse(self):
        self.setupPins(False, True, False, True)

    def turn_right(self):
        self.setupPins(False, False, False, True)

    def turn_left(self):
        self.setupPins(False, True, False, False)

    def stop_motor(self):
        self.setupPins(False, False, False, False)

    def changeSpeed(self, dutyCycle):
        self.pwm.ChangeDutyCycle(dutyCycle)

    def setupPins(self, mrf, mrr, mlf, mlr):
        gpio.output(self.motorPins.getMotorRightReverse(), mrr)
        gpio.output(self.motorPins.getMotorRightForward(), mrf)
        gpio.output(self.motorPins.getMotorLeftForward(), mlf)
        gpio.output(self.motorPins.getMotorLeftReverse(), mlr)


