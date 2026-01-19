import os
import json

FILES = [
    "storage/index.json",
    "storage/metadata.json",
    "storage/dependencies.json",
]

def reset():
    os.makedirs("storage", exist_ok=True)

    for path in FILES:
        with open(path, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=2)
        print(f"Cleared: {path}")

    print("\nStorage reset to empty objects {}.")

if __name__ == "__main__":
    reset()
