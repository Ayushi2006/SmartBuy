import json

def load_products():
    with open("data.json") as f:
        return json.load(f)
    
def get_products(query):
    data = load_products()

    filtered = [p for p in data if query.lower() in p["name"].lower()]
    print("using local dataset...")

    return filtered if filtered else data