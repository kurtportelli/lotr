from main import fetch_items


def test_fetch_items():
    items = ["book", "movie", "character", "quote", "chapter"]

    for item in items:
        item_data = fetch_items(item)
        assert len(item_data['docs']) == item_data['total']
