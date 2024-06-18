from fastapi import FastAPI

from pydantic import BaseModel, validator, ValidationError
from auth import auth_router
from product import product_router
from order import order_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(order_router)


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None
    tags: list[str] = []


try:
    Item()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))


@app.post('/items/')
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="computer", price=1200.1, description='this is computer'),
        Item(name="phone", price=130.4, description='this is phone')
    ]
