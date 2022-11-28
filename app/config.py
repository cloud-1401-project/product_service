from fastapi import FastAPI
import databases
import sqlalchemy
import grpc
import auth_pb2_grpc
import auth_pb2
import asyncio

loop = asyncio.get_event_loop()

''' GRPC CONFIGURATION '''
GRPC_URL = "auth_grpc_server:50051"
Resource = auth_pb2.Resource
channel = grpc.insecure_channel(GRPC_URL)
stub = auth_pb2_grpc.AuthServiceStub(channel)

''' FastAPI CONFIGURATION '''
app = FastAPI(title="Product Service",
              docs_url="/api/products/docs", redoc_url="/api/products/redocs")


''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://fastapi:123456@product_service_database:5432/fastapi"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

''' APP EVENT SETTING'''


def sync_start_up():
    loop.run_until_complete(database.connect())


def sync_shut_down():
    loop.run_until_complete(database.disconnect())


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
