from pydantic import BaseModel, condecimal
from decimal import Decimal
from app.models.item_status import ItemStatus

class ItemBase(BaseModel):
    name: str
    price: condecimal(max_digits=10, decimal_places=2)

class Item(ItemBase):
    id: int
    status: ItemStatus