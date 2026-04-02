import json
import os

def load_products():
    # Get the current file's directory (backend folder)
    base_dir = os.path.dirname(__file__)
    
    # Create full path to data.json
    data_path = os.path.join(base_dir, "data.json")

    # Check if data.json exists
    if not os.path.exists(data_path):
        print("⚠️ data.json not found! Please generate data first.")
        return []

    # Open and read the JSON file
    with open(data_path, "r", encoding="utf-8") as f:
        try:
            # Load JSON data into Python list
            data = json.load(f)
        except json.JSONDecodeError:
            # Handle case when file is empty or corrupted
            print("⚠️ data.json is empty or invalid! Please regenerate it.")
            return []

    # Return the list of products
    return data