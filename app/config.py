from fastapi import FastAPI
import databases
import sqlalchemy
import grpc
import auth_pb2_grpc

''' GRPC CONFIGURATION '''
stub = None
GRPC_URL = "localhost:50051"

''' FastAPI CONFIGURATION '''
app = FastAPI(title="Product Service",
              docs_url="/api/products/docs", redoc_url="/api/products/redocs")


''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://fastapi:123456@127.0.0.1:5432/fastapi"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)


''' APP EVENT SETTING'''


@app.on_event("startup")
async def startup():
    global stub
    await database.connect()
    channel = grpc.insecure_channel(GRPC_URL)
    stub = auth_pb2_grpc.AuthServiceStub(channel)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
