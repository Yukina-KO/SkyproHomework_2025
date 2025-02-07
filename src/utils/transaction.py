import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_transactions() -> None:
    file_path = os.path.join(BASE_DIR, "data", "operations.json")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        print(item)
