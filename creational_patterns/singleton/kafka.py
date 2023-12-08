from kafka import KafkaProducer
import json

class KafkaProducerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(KafkaProducerSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, kafka_servers):
        # This will only be executed once
        self.producer = KafkaProducer(bootstrap_servers=kafka_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def send_message(self, topic, value):
        self.producer.send(topic, value)
        self.producer.flush()

# Usage example
kafka_servers = ['localhost:9092']  # Replace with your Kafka server addresses
producer1 = KafkaProducerSingleton(kafka_servers)
producer2 = KafkaProducerSingleton(kafka_servers)

print(producer1 == producer2)  # True

# Sending a message
producer1.send_message('my_topic', {'key': 'value'})
