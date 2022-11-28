from fastapi import APIRouter
from typing import List
from config import database
from .model import products
from .schema import Product
import string
import random


def gen_rand_str():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


products_route = APIRouter()


@products_route.get("/all", response_model=List[Product], status_code=200)
async def all_products():
    query = products.select()
    all_products = await database.fetch_all(query)
    if products is None:
        return {"message": " No post found!"}
    else:
        return all_products


@products_route.post("/create_random_products", status_code=200)
async def create_random_products():
    for _ in range(5):
        query = products.insert().values(title=gen_rand_str(), count_in_storage=random.randint(0, 100))
        await database.execute(query=query)
