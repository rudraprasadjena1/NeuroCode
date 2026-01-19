#scanner\cache.py
import json
import os

INDEX_PATH = "storage/index.json"
METADATA_PATH = "storage/metadata.json"
DEPS_PATH = "storage/dependencies.json"


def load_index():
    if not os.path.exists(INDEX_PATH):
        return {}
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index(data):
    os.makedirs("storage", exist_ok=True)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_metadata():
    if not os.path.exists(METADATA_PATH):
        return {}
    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_metadata(data):
    os.makedirs("storage", exist_ok=True)
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def save_dependencies(data):
    os.makedirs("storage", exist_ok=True)
    with open(DEPS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
