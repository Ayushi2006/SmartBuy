import json
import random

# Realistic names for each category
products_data = {
    "phone": [
        ("Samsung", ["Galaxy S23", "Galaxy A54", "Galaxy M14"]),
        ("Xiaomi", ["Redmi Note 13", "Mi 13", "Poco X5"]),
        ("Realme", ["GT Neo 5", "C55", "Narzo 60"]),
        ("Apple", ["iPhone 14", "iPhone 13"]),
        ("OnePlus", ["OnePlus 11", "OnePlus Nord 3"])
    ],
    "laptop": [
        ("Dell", ["Inspiron 15", "XPS 13"]),
        ("HP", ["Pavilion 14", "Envy 13"]),
        ("Lenovo", ["IdeaPad 5", "ThinkPad X1"]),
        ("Asus", ["VivoBook 15", "ROG Strix"]),
        ("Apple", ["MacBook Air", "MacBook Pro"])
    ],
    "watch": [
        ("Fossil", ["Gen 6", "Hybrid HR"]),
        ("Titan", ["Edge", "Neo"]),
        ("Casio", ["G-Shock", "Edifice"]),
        ("Apple", ["Watch Series 9", "Watch SE"]),
        ("Samsung", ["Galaxy Watch 6", "Galaxy Fit 2"])
    ],
    "clothes": [
        ("Nike", ["Air Hoodie", "Sports T-Shirt"]),
        ("Adidas", ["Running Shorts", "Track Jacket"]),
        ("Levi's", ["Slim Jeans", "Trucker Jacket"]),
        ("Puma", ["Sports Hoodie", "T-Shirt"]),
        ("H&M", ["Casual Shirt", "Denim Jeans"])
    ],
    "accessories": [
        ("Sony", ["Wireless Earbuds", "Portable Speaker"]),
        ("Logitech", ["Gaming Mouse", "Mechanical Keyboard"]),
        ("Generic", ["Phone Case", "USB Cable"]),
        ("Samsung", ["Galaxy Buds", "Wireless Charger"])
    ]
}

all_products = []

# Generate ~20 products per category
for category, brand_models in products_data.items():
    for brand, models in brand_models:
        for model in models:
            # Random variations for multiple products
            for i in range(2):  # 2 products per model for variety
                price = 0
                if category == "phone":
                    price = random.randint(8000, 50000)
                elif category == "laptop":
                    price = random.randint(25000, 150000)
                elif category == "watch":
                    price = random.randint(2000, 50000)
                elif category == "clothes":
                    price = random.randint(500, 5000)
                elif category == "accessories":
                    price = random.randint(300, 5000)

                rating = round(random.uniform(3.5, 5.0), 1)
                reviews = random.randint(50, 5000)
                shipping = random.randint(30, 500)
                delivery_days = random.randint(1, 10)

                name = f"{brand} {model}"

                all_products.append({
                    "name": name,
                    "price": price,
                    "rating": rating,
                    "reviews": reviews,
                    "brand": brand,
                    "category": category,
                    "shipping": shipping,
                    "delivery_days": delivery_days
                })

# Shuffle list to randomize
random.shuffle(all_products)

# Save to JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(all_products, f, indent=2)

print(f"data.json with {len(all_products)} realistic products generated successfully!")