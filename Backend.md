# SmartBuy Backend

This repository contains the **backend logic** for SmartBuy AI-powered product recommendation.

The backend provides:  
- Multi-category support: **phones, clothes, electronics**  
- **Budget filtering** from user queries  
- **Deal scoring formula** to rank products  
- **JSON API** ready for frontend integration  
- Optional CLI for local testing

---

## Folder Structure
SmartBuy/
├─ app.py # Flask API entrypoint
├─ test.py # CLI testing interface
├─ assistant.py # Main backend logic
├─ query_parser.py # Parses queries into category & budget
├─ scorer.py # Ranking/score logic
├─ data_fetcher.py # Loads data.json
├─ data.json # Sample product dataset
├─ requirements.txt # Python dependencies


---

## Installation

1. Clone the repository:

`git clone <your-backend-repo-url>`
`cd SmartBuy`

2. Install dependencies:

`pip install -r requirements.txt`

### Running the Backend
#### Flask API

Start the server:

`python app.py`

- Endpoint: http://127.0.0.1:5000/search
- Query parameter: query

- Example queries:

`/search?query=best+phone+under+30000`
`/search?query=best+clothes+under+3000`
`/search?query=best+electronics+under+5000`

#### Sample JSON Response:

[
    {
        "name": "Redmi 12C",
        "price": 9500,
        "rating": 4.2,
        "reviews": 1800,
        "brand": "Xiaomi",
        "category": "phone",
        "shipping": 150,
        "delivery_days": 4,
        "score": 4732.6
    }
]

## CLI Testing (Optional)

#### Run:

`python test.py`
- Enter queries like: best phone under 30000 or best electronics under 5000
- See ranked product list in terminal
- Type exit to quit

### Integration Notes for Frontend Team
- API Base URL: http://127.0.0.1:5000/search
- Query parameter: query
- Response: JSON array of products including score for ranking
- Products are filtered by category and budget, and sorted by score (lower score = better deal)

### Scoring Formula:
- Score = (Price × 0.5) + (Shipping × 0.1) + (Delivery Time × 0.2) − (Rating × weight)

- weight defaults to 10
- Lower score = better deal

## Adding Products / Categories
- Add new products in data.json
- Add new categories (e.g., furniture, books) in query_parser.py under category detection

## License / Notes
- Backend only (CLI + Flask API)
- Ready for integration with frontend frameworks like React

