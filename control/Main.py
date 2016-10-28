from messaging.MessagePublisher import MessagePublisher
from messaging.RPCBridge import RPCBridge
from messaging.MessageHook import MessageHook
from motion.motion_control.KineticContext import KineticContext
import asyncio
from concurrent.futures.ThreadPoolExecutor import ThreadPoolExecutor
from scheduler.AsyncScheduler import AsyncScheduler
from scheduler.Scheduler import Scheduler
from scheduler.BlockingScheduler import BlockingScheduler

messagePublisher = MessagePublisher()
messageHook = MessageHook(messagePublisher)
rpcBridge = RPCBridge("tcp://0.0.0.0:4242", messageHook)

kineticContext = KineticContext()
 
executor = ThreadPoolExecutor(
    max_workers=3,
)
 
event_loop = asyncio.get_event_loop()
blockingScheduler = BlockingScheduler(asyncio, event_loop, executor)
asyncScheduler = AsyncScheduler(asyncio, 1)
scheduler = Scheduler()

try:
    event_loop.run_forever()    
finally:
    event_loop.close()    


# import zerorpc
# from motor_control.MotorControl import MotorControl
# from motor_control.MotorIO import MotorIO, MotorPins
# from sensor_consumer.LastSensorDataProvider import LastSensorDataProvider
# import _thread
# import time
# from motor_control.MotorThread import MotorThread
# from motor_control.MotorSpeedUp import MotorSpeedUp, SpeedUpValues
# from motor_control.MotorControl import MotorControl
# 
# motorIO = MotorIO(MotorPins())
# motorSensorDataProvider = LastSensorDataProvider()
# motorThread = MotorThread(_thread.start_new_thread, time)
# speedUpValues = SpeedUpValues([30, 50, 80], [0.2, 0.2, 0.2])
# motorSpeedUp = MotorSpeedUp(motorIO, speedUpValues, time)
# motorControl = MotorControl(motorIO, motorSensorDataProvider)
# motorThread.start(motorSensorDataProvider, motorSpeedUp.speedUp, 1)
# 
# class HelloRPC(object):
#     def hello(self, name):
#         return "Hello, %s" % name
# 
#     def forward(self):
#         return motorControl.forward()
# 
#     def reverse(self):
#         return motorControl.reverse()
# 
#     def turn_left(self):
#         return motorControl.turn_left()
# 
#     def turn_right(self):
#         return motorControl.turn_right()
# 
#     def stop_motor(self):
#         return motorControl.stop_motor()
#     
#     def cleanup(self):
#         gpio.cleanup()
# 
# s = zerorpc.Server(HelloRPC())
# s.bind("tcp://0.0.0.0:4242")
# s.run()

