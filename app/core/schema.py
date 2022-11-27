from pydantic import BaseModel


''' Model Schema Using Pydantic '''


class Product(BaseModel):
    id: int
    title: str
    count: int
