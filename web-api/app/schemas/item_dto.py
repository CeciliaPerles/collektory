from pydantic import BaseModel
from decimal import Decimal
from app.models.item_status import ItemStatus

class ItemBase(BaseModel):
    name: str
    price: Decimal

    def __init__(self, name: str, price: Decimal, /, **data):
        super().__init__(**data)
        self.name = name
        self.price = price

class Item(ItemBase):
    id: int
    status: ItemStatus

    def __init__(self, id: int, status: ItemStatus, name: str, price: Decimal):
        super().__init__(name, price)
        self.id = id
        self.status = status