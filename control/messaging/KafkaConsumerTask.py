from kafka import KafkaConsumer
import json
import sys

class KafkaConsumerTask:
    
    def __init__(self, messagePublisher):
        self.kafkaConsumer = KafkaConsumer('test',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])
        self.messagePublisher = messagePublisher
        
    def execute(self):
        print('before')
        for msg in self.kafkaConsumer:
            print(msg)
#             self.messagePublisher.dispatch(
#                 {
#                     category: 'MOTION',
#                     direction: 'FORWARD'
#                 }
#             )
#             {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
            try:
                msgDecoded = json.loads(msg.value.decode("utf-8"))
                self.messagePublisher.dispatch(msgDecoded)    
            except:
                e = sys.exc_info()[0]
                print(e)