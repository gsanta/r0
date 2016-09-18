import zerorpc
from motor_control.MotorControl import MotorControl
from motor_control.MotorIO import MotorIO, MotorPins
from sensor_consumer.LastSensorDataProvider import LastSensorDataProvider
import _thread
import time
from motor_control.MotorThread import MotorThread
from motor_control.MotorSpeedUp import MotorSpeedUp, SpeedUpValues
from motor_control.MotorControl import MotorControl

motorIO = MotorIO(MotorPins())
motorSensorDataProvider = LastSensorDataProvider()
motorThread = MotorThread(_thread.start_new_thread, time)
speedUpValues = SpeedUpValues([30, 50, 80], [0.2, 0.2, 0.2])
motorSpeedUp = MotorSpeedUp(motorIO, speedUpValues, time)
motorControl = MotorControl(motorIO, motorSensorDataProvider)
motorThread.start(motorSensorDataProvider, motorSpeedUp.speedUp, 1)

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

