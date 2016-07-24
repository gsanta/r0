import zerorpc
import motor_control as motor
import RPi.GPIO as gpio
import time

motorPins = motor.MotorPins()
motorPins.setPWM(12)
motorPins.setMotorRightForward(11)
motorPins.setMotorRightReverse(7)
motorPins.setMotorLeftForward(13)
motorPins.setMotorLeftReverse(15)
motorControl = motor.MotorControl(motorPins)

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

    def forward(self):
        return motorControl.forward()

    def reverse(self):
        return motorControl.reverse()

    def turn_left(self):
        return motorControl.turn_left()

    def turn_right(self):
        return motorControl.turn_right()

    def stop_motor(self):
        return motorControl.stop_motor()
    
    def cleanup(self):
        gpio.cleanup()

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()

