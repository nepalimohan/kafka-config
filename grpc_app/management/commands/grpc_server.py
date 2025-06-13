# grpc_app/management/commands/grpc_server.py
from django.core.management.base import BaseCommand
import grpc
from concurrent import futures
import time

from grpc_app.services import example_pb2_grpc
from grpc_app.services.servicer import GreeterServicer

class Command(BaseCommand):
    help = "Starts gRPC server"

    def handle(self, *args, **kwargs):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        example_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        self.stdout.write(self.style.SUCCESS("gRPC server started on port 50051"))
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            server.stop(0)
