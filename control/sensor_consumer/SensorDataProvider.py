

class DistanceDataProvider(object):
    
    __init__(self, dataHandlerCommand):
	self.dataHandlerCommand = dataHandlerCommand
	self.prevData = None

    pushData(self, data):.
        if data != self.prevData):
	    self.prevData = prevData
	    self.dataHandlerCommand.execute(data)

    
        

class QueuedSensorDataProvider(object):

    __init__(self, dataQueue):
	self.dataQueue = dataQueue
	self.distanceDataProvider = 

    getDistanceDataProvider(self):
	

    
