from app.data.item_data import fetch_items, store_item

def get_items_handler():
    # Handler logic to get items
    return fetch_items()

def create_item_handler(item: dict):
    if not item or not item["name"]:
        raise ValueError("Invalid input data")

    # Handler logic to create a new item
    return store_item(item)
