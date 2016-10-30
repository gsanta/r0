

class MessagePublisher:
    
    def __init__(self):
        self.subscribers = set()
        self.message = None

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)
        
    def getMessage(self):
        return self.message
    
    def dispatch(self, message):
        self.message = message
        for subscriber in self.subscribers:
            subscriber.notify()


