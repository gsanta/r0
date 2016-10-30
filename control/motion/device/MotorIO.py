import RPi.GPIO as gpio

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
        self._setPins(True, False, True, False)

    def reverse(self):
        self._setPins(False, True, False, True)

    def turnRight(self):
        self._setPins(False, False, False, True)

    def turnLeft(self):
        self._setPins(False, True, False, False)

    def stopMotor(self):
        self._setPins(False, False, False, False)

    def changeSpeed(self, dutyCycle):
        self.pwm.ChangeDutyCycle(dutyCycle)

    def _setPins(self, mrf, mrr, mlf, mlr):
        gpio.output(self.motorPins.getMotorRightReverse(), mrr)
        gpio.output(self.motorPins.getMotorRightForward(), mrf)
        gpio.output(self.motorPins.getMotorLeftForward(), mlf)
        gpio.output(self.motorPins.getMotorLeftReverse(), mlr)


