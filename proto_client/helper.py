import grpc
import product_pb2
import product_pb2_grpc


def get_product(stub):
    p = stub.GetProduct(product_pb2.PID(id=2000))
    print(f'p is {p}')


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        get_product(stub)
        
run()