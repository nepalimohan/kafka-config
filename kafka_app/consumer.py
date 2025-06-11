from confluent_kafka import Consumer
from django.conf import settings

def consume_messages():
    consumer = Consumer({
        'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'django-group',
        'auto.offset.reset': 'earliest'
    })

    consumer.subscribe([settings.KAFKA_TOPIC])

    print("Started consuming...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            print('Received message: {}'.format(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
