from fastapi import APIRouter, HTTPException
from typing import List

from models.item import Item, Item_Response


router = APIRouter()

# Sample data store
items_db: List[Item] = [
    Item(id=1, name="Laptop", description="A powerful laptop", price=999.99),
    Item(id=2, name="Mouse", description="Wireless mouse", price=29.99),
    Item(id=3, name="Keyboard", price=79.99),
]


@router.get("/", response_model=List[Item_Response])
def get_all_items():
    """Return a list of all available items."""
    return items_db


@router.get("/{id}", response_model=Item_Response)
def get_item_by_id(id: int):
    """Return an item by its ID."""
    for item in items_db:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
