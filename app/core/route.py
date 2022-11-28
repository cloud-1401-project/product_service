from fastapi import APIRouter, Header
from typing import List
from config import database
from .model import products
from .schema import Product
from core.auth import has_access
from fastapi.responses import JSONResponse
import string
import random


def gen_rand_str():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


products_route = APIRouter()


@products_route.get("/all", response_model=List[Product], status_code=200)
async def all_products(authorization: str | None = Header(default=None)):
    if authorization is None or has_access('GET', "/api/products/all", authorization) == False:
        return JSONResponse(status_code=401,
                            content={"message": "You don't have access to this resource."})
    query = products.select()
    all_products = await database.fetch_all(query)
    if products is None:
        return {"message": " No post found!"}
    else:
        return all_products


@products_route.post("/create_random_products", status_code=200)
async def create_random_products(authorization: str | None = Header(default=None)):
    if authorization is None or has_access('POST', "/api/products/create_random_products", authorization) == False:
        return JSONResponse(status_code=401,
                            content={"message": "You don't have access to this resource."})
    for _ in range(5):
        query = products.insert().values(title=gen_rand_str(), count_in_storage=random.randint(0, 100))
        await database.execute(query=query)
