# assistant.py
from data_fetcher import load_products
from query_parser import parse_query
from scorer import rank_products

def shopping_assistant(query):
    data = load_products()
    intent = parse_query(query)

    # Filter by category & budget
    filtered = [
        p for p in data
        if (not intent["category"] or p.get("category") == intent["category"])
        and (not intent["budget"] or p.get("price", 0) <= intent["budget"])
    ]

    # Rank products using scorer (optional)
    ranked = rank_products(filtered)

    return ranked