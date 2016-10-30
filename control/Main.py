# from messaging.MessagePublisher import MessagePublisher
from messaging.MessagePublisher import MessagePublisher
from motion.motion_control.KineticContext import KineticContext
import asyncio
from concurrent.futures import ThreadPoolExecutor
from scheduler.AsyncScheduler import AsyncScheduler
from scheduler.Scheduler import Scheduler
from scheduler.BlockingScheduler import BlockingScheduler
from messaging.SocketIOServer import SocketIOServer
from messaging.SocketIOEventHandler import SocketIOEventHandler
from motion.messaging.MotorMessageSubscriber import MotorMessageSubscriber
from motion.messaging.MotorMessageProcessor import MotorMessageProcessor
from motion.driver.MotorDriver import MotorDriver
from motion.motion_control.KineticStateFactory import KineticStateFactory
from motion.device.MotorControl import MotorControl
from motion.device.DummyMotorIO import DummyMotorIO
from motion.device.MotorPins import MotorPins

executor = ThreadPoolExecutor(
    max_workers=3,
)
 
event_loop = asyncio.get_event_loop()
blockingScheduler = BlockingScheduler(asyncio, event_loop, executor)
asyncScheduler = AsyncScheduler(asyncio, 1)
scheduler = Scheduler()

messagePublisher = MessagePublisher()
kineticContext = KineticContext()

motorDriver = MotorDriver(kineticContext, scheduler)
kineticStateFactory = KineticStateFactory(MotorControl(DummyMotorIO()), kineticContext)
motorMessageProcessor = MotorMessageProcessor(motorDriver, kineticStateFactory)
motorMessageSubscriber = MotorMessageSubscriber(messagePublisher, motorMessageProcessor)

socketIOServer = SocketIOServer(SocketIOEventHandler(messagePublisher))
socketIOServer.run()