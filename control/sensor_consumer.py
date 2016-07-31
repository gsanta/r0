import Queue
from threading import Thread
class SensorDataConsumer(Thread):
    
    def __init__(self, distanceQueue):
        Thread.__init__(self)
        self.distanceQueue = distanceQueue

    def run(self):

        while True:
            print 'distance ', self.distanceQueue.get(), 'cm'



class SensorDataConsumerWrapper():
    
    def __init__(self, distanceQueue):
        self.distanceQueue = distanceQueue
        self.thread = SensorDataConsumer(self.distanceQueue)

    def start(self):
        self.thread.start()
