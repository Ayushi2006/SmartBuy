import re

def parse_query(query):
    query = query.lower()

    budget = None

    match = re.search(r'(\d+)k', query)
    if match:
        budget = int(match.group(1))*1000

    category = "phone" if "phone" in query else None

    return{
        "budget": budget,
        "category": category
    }