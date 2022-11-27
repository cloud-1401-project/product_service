from concurrent import futures
import product_pb2_grpc
import grpc


class ProductServiceServer(product_pb2_grpc.ProductServiceServicer):
    def GetProduct(self, request, context):
        print(f"req is {request} and con is {context}")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  product_pb2_grpc.add_ProductServiceServicer_to_server(
      ProductServiceServer(), server)
  server.add_insecure_port('localhost:50051')
  server.start()
  server.wait_for_termination()

serve()