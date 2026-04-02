# assistant.py
from data_fetcher import load_products
from query_parser import parse_query  # Make sure this exists and is correct

def shopping_assistant(query):
    # Parse the user query
    intent = parse_query(query)

    category = intent.get("category")
    budget = intent.get("budget")

    # Load all products
    data = load_products()

    # Filter by category if provided
    if category:
        filtered = [p for p in data if p.get("category") == category]
    else:
        filtered = data

    # Further filter by budget
    if budget:
        filtered = [p for p in filtered if p.get("price", 0) <= budget]

    # Fallback if nothing matches
    if not filtered:
        print(f"⚠️ Category '{category}' not found or no products in budget. Try something else!")
        return []

    return filtered