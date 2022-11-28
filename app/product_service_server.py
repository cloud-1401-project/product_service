from concurrent import futures
import product_pb2_grpc
import product_pb2
import grpc
import config
import asyncio
from config import database, loop, metadata, engine
from core.model import products
from core.schema import Product
from core.schema import Product


class ProductServiceServer(product_pb2_grpc.ProductServiceServicer):
    def GetProduct(self, request, context):
        query = products.select().where(products.c.id == request.id)
        res = loop.run_until_complete(database.fetch_one(query=query))
        if res is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Provided ID is not valid.')
            return product_pb2.PInfo()
        return product_pb2.PInfo(title=res.title, count=res.count_in_storage)

def serve():
    metadata.create_all(engine)
    config.sync_start_up()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(
      ProductServiceServer(), server)
    server.add_insecure_port('0.0.0.0:50052')
    server.start()
    server.wait_for_termination()
    config.sync_shut_down()

serve()