import grpc
from grpc_app.services import example_pb2_grpc, example_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = example_pb2_grpc.GreeterStub(channel)

response = stub.SayHello(example_pb2.HelloRequest(name='Mohan'))
print(response.message)
