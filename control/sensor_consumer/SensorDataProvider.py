import Queue

class LastSensorDataProvider(object):

    __init__(self):
	self.data = None

    addData(self, data):
        self.data = data

    popData():
        data = self.data
        self.data = None
        return data
	

    
