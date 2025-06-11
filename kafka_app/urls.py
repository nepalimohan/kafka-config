from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.send_kafka_message),
]
