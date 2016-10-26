import unittest
from MotorMessageSubscriber import MotorMessageSubscriber

class MessagePublisherStub:
    def __init__(self, message):
        self.message = message
        self.subscribed = False

    def getMessage(self):
        return self.message

    def subscribe(self, obj):
        self.subscribed = True

class MessageProcessorStub:
    def __init__(self):
        self.processed = False

    def process(self, message):
        self.processed = True

class MessageStub:

    def __init__(self, category):
        self.category = category
        self.command = None

class MotorMessageSubscriberSpec(unittest.TestCase):

    def testNotifyNoProcess(self):
        message = MessageStub('somethingElse') 
        publisher = MessagePublisherStub(message)
        processor = MessageProcessorStub()
        subscriber = MotorMessageSubscriber(publisher, processor)
        subscriber.notify()
        self.assertTrue(processor.processed == False)
        self.assertTrue(publisher.subscribed == True)

    def testNotifyDoProcess(self):
        message = MessageStub('motion') 
        publisher = MessagePublisherStub(message)
        processor = MessageProcessorStub()
        subscriber = MotorMessageSubscriber(publisher, processor)
        subscriber.notify()
        self.assertTrue(processor.processed == True)
        self.assertTrue(publisher.subscribed == True)


if __name__ == '__main__':
    unittest.main()
