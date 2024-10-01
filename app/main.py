# app/main.py
from fastapi import FastAPI
from app.handlers.item_handler import get_items_handler, create_item_handler

app = FastAPI()

@app.get("/items")
async def get_items():
    return get_items_handler()

@app.post("/items")
async def create_item(item: dict):
    return create_item_handler(item)

