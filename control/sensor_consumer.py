import Queue
from threading import Thread

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

    def run(self):

        while True:
            distance = self.distanceQueue.get()
            print 'distance ', self.distanceQueue.get(), 'cm'
            if distance < 40:
                self.motorChannel.push('left')



class SensorDataConsumerWrapper(object):
    
    def __init__(self, distanceQueue, motorChannel):
        self.distanceQueue = distanceQueue
        self.motorChannel = motorChannel
        self.thread = SensorDataConsumer(self.distanceQueue, self.motorChannel)

    def start(self):
        self.thread.start()
