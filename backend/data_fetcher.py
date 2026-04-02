import json
import os

def load_products():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data.json")

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data

def get_products(query):
    data = load_products()

    filtered = [p for p in data if query.lower() in p["name"].lower()]
    print("using local dataset...")

    return filtered if filtered else data