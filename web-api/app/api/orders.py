import decimal
from decimal import Decimal

from fastapi import APIRouter
from app.models.item_status import ItemStatus
from random import randint
import random
from app.schemas.item_dto import Item
from app.schemas.item_list_response import ItemListResponse

router = APIRouter()

@router.get("/{id}/items")
def get_order_items(id: int, status: ItemStatus):

    id_1:int = randint(0, 1000)
    price_1: float = random.uniform(2000,3000)
    price_decimal_1 = decimal.Decimal(price_1)

    item_1 = Item(id_1, status, "Item " + str(id_1), price_decimal_1)

    id_2 = randint(0, 1000)
    item_2 = Item(id_2, status, "Item " + str(id_2), price_decimal_1)

    items_list = ItemListResponse(items=[item_1, item_2])

    return items_list



