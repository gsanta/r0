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
