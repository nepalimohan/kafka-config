from confluent_kafka import Producer
from django.conf import settings
import json

producer = Producer({'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS})

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed:', err)
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_message(topic, value):
    # producer.produce(topic, value.encode('utf-8'), callback=delivery_report)
    producer.produce(topic, json.dumps(value).encode('utf-8'))
    producer.flush()
