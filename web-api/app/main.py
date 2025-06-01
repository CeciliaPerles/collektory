from fastapi import FastAPI
from app.api import orders

app = FastAPI()

app.include_router(orders.router, prefix="/api/orders", tags=["orders"])


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

