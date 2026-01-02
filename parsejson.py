import json
from pathlib import Path

def load_json(json_path, items_key):
    file = Path(json_path).open("r", encoding="utf-8")
    data = json.load(file)
    file.close()
    items = data[items_key]
    return items
