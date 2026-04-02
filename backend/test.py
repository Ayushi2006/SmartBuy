from assistant import shopping_assistant

query = "best phone under 50k"

print("User Query:", query)

products, best = shopping_assistant(query)

print("\nRecommended Products")

for p in products:
    print(f"-{p['name']}, Rs{p['price']}, {p.get('rating', 'N/A')}, Reviews:{p.get('reviews', 0)}")
if best:
    print("\nAI Recommendation:")
    print(f"{best['name']} is the best option under your budget with rating {best.get('rating', 'N/A')} and strong overall value (Score: {best['score']}).")
else:
    print("\nNo suitable product found.")