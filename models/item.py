from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


class Item_Response(BaseModel):
    id: int
    name: str
