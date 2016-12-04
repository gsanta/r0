from DistanceMessage import DistanceMessage

class DistanceProcessor:
    
    def __init__(self, messagePublisher):
        self.messagePublisher = messagePublisher
        
    def setData(self, data):
        message = DistanceMessage(data)
        self.messagePublisher.dispatch(message)