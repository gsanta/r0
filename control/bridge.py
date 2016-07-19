import zerorpc
import motor_control as motor
import RPi.GPIO as gpio
import time
#motor.init()

print "motor init"
motor.init()
print "motor forward"
motor.forward()
time.sleep(10)
print "program ending"
gpio.cleanup()

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

    def forward(self):
        return motor.forward()

    def reverse(self):
        return motor.reverse()

    def turn_left(self):
        return motor.turn_left()

    def turn_right(self):
        return motor.turn_right()

    def stop_motor(self):
        return motor.stop_motor()
    
    def cleanup(self):
        gpio.cleanup()

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()

