# 🛒 SmartBuy AI – Intelligent Price Comparison Engine

## 🚀 Overview

SmartBuy AI is a web-based intelligent shopping assistant that helps users find the best product deals across multiple e-commerce platforms.

Instead of manually comparing prices, delivery times, and ratings, SmartBuy AI automatically aggregates, analyzes, and recommends the best option using a smart scoring system.

---

## 🎯 Problem Statement

Online shoppers often waste time opening multiple tabs to compare the same product across platforms like Amazon, Flipkart, and others.

This leads to:

- Confusion due to inconsistent pricing
- Difficulty in comparing delivery times and ratings
- Uncertainty about the best purchase decision

---

## 💡 Solution

SmartBuy AI simplifies this process by:

- Fetching product data from multiple sources
- Matching similar products intelligently
- Normalizing and comparing key attributes
- Computing the best deal using a scoring algorithm
- Providing clear recommendations with reasoning

---

## 🔥 Key Features

- 🔍 Product Search (by name or query)
- 🔗 Multi-platform comparison (Amazon, Flipkart, etc.)
- ⚖️ Smart scoring algorithm for ranking
- 🥇 Best deal recommendation
- 📊 Clean comparison table UI
- 🤖 AI-generated explanation (optional)
- 🛟 Fallback system using mock dataset (ensures reliability)

---

## 🧠 How It Works

1. User enters a product query (e.g., "iPhone 13")
2. Backend fetches product data (API or mock dataset)
3. Matching engine filters relevant products
4. Data is normalized into a standard format
5. Scoring algorithm evaluates each product
6. Products are ranked based on computed score
7. Best option is highlighted
8. Results are displayed in a clean UI

---

## 🏗️ System Architecture

User (React UI)
↓
Search Request (/search API)
↓
FastAPI Backend
↓
Data Fetch Layer (API + Mock Data)
↓
Matching Engine
↓
Normalization Engine
↓
Scoring Engine
↓
Recommendation Engine
↓
(Optional) AI Explanation
↓
JSON Response
↓
Frontend Display

---

## 🧩 Tech Stack

### Frontend

- React
- Tailwind CSS
- Axios

### Backend

- FastAPI (Python)
- RapidFuzz (for fuzzy matching)
- Requests (for API calls)

### Optional

- OpenAI API (for generating explanations)

---

## ⚙️ Scoring Logic

The system computes a score for each product using:

Score =
(Price × 0.5) +
(Shipping × 0.1) +
(Delivery Time × 0.2) −
(Rating × weight)

Lower score indicates a better deal.

---

## 📁 Project Structure

```
frontend/
  ├── src/
  │   ├── components/
  │   ├── pages/
  │   ├── services/
  │   ├── utils/
  │   └── App.jsx

backend/
  ├── app/
  │   ├── routes/
  │   ├── services/
  │   ├── models/
  │   ├── utils/
  │   └── data/
  │       └── mock_data.json
```

---

## 🛠️ Setup Instructions

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🔌 API Endpoint

### POST `/search`

#### Request:

```json
{
  "query": "iPhone 13"
}
```

#### Response:

```json
[
  {
    "platform": "Flipkart",
    "price": 51499,
    "delivery_days": 3,
    "rating": 4.4,
    "score": 12345
  }
]
```

---

## ⚠️ Limitations

- Real-time scraping may fail due to anti-bot protections
- Product matching is approximate (string-based)
- Data may vary slightly across platforms
- Mock dataset used as fallback for reliability

---

## 🚀 Future Improvements

- Real-time multi-site scraping with resilience
- Personalized recommendations based on user preferences
- Price history tracking and alerts
- Browser extension integration
- Advanced AI-based product matching

---

## 👥 Team Roles

- Frontend Developer (UI/UX)
- Backend Developer (API & Server)
- Data Engineer (API Integration / Data Fetching)
- Logic Engineer (Matching & Scoring)
- Integration Lead (Explanation + Demo)

---

## 🏁 Demo Flow

1. Enter a product name in the search bar
2. View products from multiple platforms
3. Compare prices, delivery, and ratings
4. See the best deal highlighted
5. Read explanation of why it's recommended

---

## 🎯 Conclusion

SmartBuy AI transforms online shopping from a manual, confusing process into a fast, intelligent decision-making experience.

It combines data aggregation, algorithmic scoring, and clean UI to help users confidently choose the best product.

---

🔥 Built for Hackathon | Fast • Smart • Reliable
