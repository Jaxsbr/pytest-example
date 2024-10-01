from app.data.item_data import fetch_items, store_item

def test_fetch_items_returns_two_dicts():
    result = fetch_items()
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Item 1"
    assert result[1]["id"] == 2
    assert result[1]["name"] == "Item 2"

def test_store_item_returns_dict_with_single_item():
    test_item = {"name": "Jojo"}
    result = store_item(test_item)
    assert result["id"] == 3
    assert result["name"] == "Jojo"
