# scorer.py

def rank_products(products):
    """
    Rank products intelligently using rating, price, and reviews.
    Returns: ranked list and best product
    """
    ranked_list = []

    for p in products:
        # Safe extraction (prevents KeyError)
        rating = p.get("rating", 0)
        price = p.get("price", 0)
        reviews = p.get("reviews", 0)

        # Intelligent scoring formula
        score = (rating * 20) + (reviews / 1000) - (price / 1000)

        # Add score to product
        p["score"] = round(score, 2)

        ranked_list.append(p)

    # Sort products by score descending
    ranked = sorted(ranked_list, key=lambda x: x.get("score", 0), reverse=True)

    # Best product
    best = ranked[0] if ranked else None

    return ranked, best