# scorer.py

def rank_products(products, weight=10):
    """
    Score = (Price × 0.5) + (Shipping × 0.1) + (Delivery Time × 0.2) − (Rating × weight)
    Lower score = better deal
    """
    ranked_list = []

    for p in products:
        price = p.get("price", 0)
        shipping = p.get("shipping", 0)
        delivery = p.get("delivery_days", 0)
        rating = p.get("rating", 0)

        score = (price * 0.5) + (shipping * 0.1) + (delivery * 0.2) - (rating * weight)
        p["score"] = round(score, 2)

        ranked_list.append(p)

    # Sort by ascending score (lower is better)
    ranked = sorted(ranked_list, key=lambda x: x["score"])
    return ranked