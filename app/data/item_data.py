# Mock database: a list of items
items_db = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

def fetch_items():
    # Logic to fetch all items from the mock DB
    return items_db

def store_item(item: dict) -> dict[str, str]:
    # Logic to store a new item in the mock DB
    new_item = {
        "id": len(items_db) + 1,
        "name": item["name"]
    }
    items_db.append(new_item)
    return new_item
