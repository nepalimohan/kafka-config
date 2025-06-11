from django.http import JsonResponse
from kafka_app.producer import send_message
from django.conf import settings

def send_kafka_message(request):
    msg = "Hello"
    data = {
        "message": "Data sent to kafka producer"
    }
    print(msg)
    send_message(settings.KAFKA_TOPIC, data)
    return JsonResponse({"status": "message sent"})
