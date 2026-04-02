# query_parser.py
import re

def parse_query(query):
    query = query.lower()
    budget = None

    # Extract number
    match = re.search(r'(\d+)\s*k?', query)
    if match:
        num = int(match.group(1))
        if 'k' in query:
            budget = num * 1000
        else:
            budget = num

    # Determine category
    if "phone" in query:
        category = "phone"
    elif "clothes" in query or "shirt" in query or "jeans" in query:
        category = "clothes"
    elif "electronics" in query or "tv" in query or "headphones" in query or "watch" in query:
        category = "electronics"
    else:
        category = None

    return {"budget": budget, "category": category}