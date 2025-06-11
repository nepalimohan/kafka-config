# kafka_app/management/commands/consume_kafka.py

from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
from django.conf import settings

class Command(BaseCommand):
    help = 'Start Kafka consumer to listen for messages.'

    def handle(self, *args, **kwargs):
        consumer = Consumer({
            'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': 'django-group',
            'auto.offset.reset': 'earliest'
        })

        consumer.subscribe([settings.KAFKA_TOPIC])
        self.stdout.write(self.style.SUCCESS("Kafka consumer started..."))

        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    self.stdout.write(self.style.ERROR(f"Consumer error: {msg.error()}"))
                    continue

                value = msg.value().decode('utf-8')
                self.stdout.write(self.style.SUCCESS(f"Received message: {value}"))

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("Kafka consumer stopped manually."))
        finally:
            consumer.close()
