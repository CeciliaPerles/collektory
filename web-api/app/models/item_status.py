from enum import Enum

class ItemStatus(Enum):
    READY_TO_SHIP = "READY_TO_SHIP"
    PENDING_INVENTORY = "PENDING_INVENTORY"
    OUT_OF_ORDER = "OUT_OF_ORDER"