import json
import os

def load_products():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data.json")

    if not os.path.exists(data_path):
        print("⚠️ data.json not found! Please generate data first.")
        return []

    with open(data_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ data.json is empty or invalid! Please regenerate it.")
            return []

    return data