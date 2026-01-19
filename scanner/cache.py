#scanner\cache.py
import json
import os

INDEX_PATH = "storage/index.json"
METADATA_PATH = "storage/metadata.json"

def load_index() -> dict:
    if not os.path.exists(INDEX_PATH):
        return {}
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index(data: dict):
    os.makedirs("storage", exist_ok=True)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_metadata() -> dict:
    if not os.path.exists(METADATA_PATH):
        return {}
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_metadata(data: dict):
    os.makedirs("storage", exist_ok=True)
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
