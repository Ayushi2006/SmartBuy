import re

def parse_query(query):
    query = query.lower()
    budget = None
    category = None

    # Parse budget like "10k" or "30000"
    match = re.search(r'(\d+)\s*k?', query)
    if match:
        budget = int(match.group(1))
        # Convert k to actual number if k is in query
        if 'k' in query:
            budget *= 1000

    # Identify category
    if "phone" in query:
        category = "phone"
    elif "laptop" in query:
        category = "laptop"
    elif "watch" in query:
        category = "watch"
    elif "clothes" in query:
        category = "clothes"
    elif "accessories" in query:
        category = "accessories"

    return {"budget": budget, "category": category}