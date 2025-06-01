from pydantic import BaseModel
from typing import List
from app.schemas.item_dto import Item

class ItemListResponse(BaseModel):
    items: List[Item]

    def __init__(self, items: List[Item]):
        super().__init__()
        self.items = items