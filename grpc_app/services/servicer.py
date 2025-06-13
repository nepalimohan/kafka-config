# grpc_app/services/servicer.py
from grpc_app.services import example_pb2_grpc, example_pb2

class GreeterServicer(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return example_pb2.HelloReply(message=f"Hello, {request.name} from Django!")
