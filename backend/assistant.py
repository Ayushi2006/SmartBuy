# assistant.py
from data_fetcher import load_products
from query_parser import parse_query
from scorer import rank_products

def shopping_assistant(query):
    data = load_products()
    intent = parse_query(query)

    filtered = []

    for p in data:
        # Safe category check
        if intent["category"] and p.get("category") != intent["category"]:
            continue
        # Budget filter
        if intent["budget"] and p.get("price", 0) > intent["budget"]:
            continue
        filtered.append(p)

    # fallback if nothing matches
    if not filtered:
        filtered = data

    # Rank products
    ranked, best = rank_products(filtered)

    return ranked, best