

class MessagePublisher:
    
    def __init__(self):
        self.subscribers = set()

    def onMessage(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.addMessage(message)


