import Queue
from threading import Thread
from motor_control import Direction

class Channel(object):
    
    def __init__(self):
        self.queue = Queue.Queue()

    def push(self, data):
        self.queue.put(data)

    def top(self):
        return self.queue.get()


class SensorDataConsumer(Thread):
    
    def __init__(self, distanceQueue, motorChannel):
        Thread.__init__(self)
        self.distanceQueue = distanceQueue
        self.motorChannel = motorChannel
        self.directionAvoidance = DirectionAvoidance(30)

    def run(self):

        self.motorChannel.push(Direction.FORWARD)

        while True:
            distance = self.distanceQueue.get()
            print 'distance: ', distance
            if self.directionAvoidance.shouldStop(distance):
                print 'stopping: ', distance
                self.motorChannel.push(Direction.STOP)

         



class SensorDataConsumerWrapper(object):
    
    def __init__(self, distanceQueue, motorChannel):
        self.distanceQueue = distanceQueue
        self.motorChannel = motorChannel
        self.thread = SensorDataConsumer(self.distanceQueue, self.motorChannel)

    def start(self):
        self.thread.start()



class DirectionAvoidance(object):
    def __init__(self, minDistance):
        self.minDistance = minDistance
             
    def shouldStop(self, distance):
        if distance <= self.minDistance:
            return True
        return False
