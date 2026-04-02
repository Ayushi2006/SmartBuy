from assistant import shopping_assistant

def main():
    print("Welcome to SmartBuy CLI AI Assistant!\n")

    while True:
        query = input("Enter your product query (type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Bye!")
            break

        products = shopping_assistant(query)

        if not products:
            print("No products found for your budget.\n")
            continue

        print(f"\n🔹 Products matching your query ({len(products)} found):")
        for p in products:
            print(f"- {p['name']}, Rs{p['price']}, Rating: {p.get('rating','N/A')}, Reviews: {p.get('reviews',0)}")

        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()