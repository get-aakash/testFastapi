from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app1 = FastAPI()


@app1.post("/items/")
async def create_item(item: Item):
    return item
