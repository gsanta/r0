class LastSensorDataProvider:

    def __init__(self):
        self.data = None

    def addData(self, data):
        self.data = data

    def popData(self):
        data = self.data
        self.data = None
        return data
	

    
