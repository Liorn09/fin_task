# Crypto Asset Recommendation API

This project provides a simple crypto asset recommendation system based on recent market data from the CoinGecko API.
It uses a heuristic scoring model to rank crypto assets by short-term investment potential — combining price momentum, market activity, and volatility.


## Flow
Data Ingestion → Modeling → Ranking → API

structure

fin_task/
│
├── data_fetcher.py          # CoinGecko data ingestion
├── notebook.ipynb           # Practice examples
├── model.py                 # Scoring / ML model
├── app.py                   # FastAPI interface or notebook
├── requirements.txt
└── README.md


## Overview

The system:

Fetches real-time cryptocurrency data from the CoinGecko API.

Computes derived indicators such as:

Momentum: 7-day price change (%)

Volume Ratio: total_volume / market_cap

Volatility: short-term risk proxy

Applies a simple scoring formula:

score
=
0.5
×
momentum
+
0.3
×
volume ratio
−
0.2
×
volatility
score=0.5×momentum+0.3×volume ratio−0.2×volatility

Ranks and returns the top recommended crypto assets.

## Why These Weights?

The weights (0.5, 0.3, −0.2) are heuristic, chosen to:

Prioritize trend (momentum) the most (50% influence).

Still reward market strength/liquidity (30%).

Penalize instability (20%).

They represent a balanced, intuitive trade-off between rewarding performance and avoiding excessive risk.



The API is exposed through FastAPI and can be accessed locally via uvicorn.

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/crypto-recommender.git
cd crypto-recommender

2️⃣ Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the API

Use uvicorn to start the FastAPI server:

uvicorn api:app --reload


By default, the API will run on:

http://127.0.0.1:8000

🔄 API Endpoint
GET /recommend

Fetches the latest crypto market data and returns top-ranked recommendations.

Example Request
GET http://127.0.0.1:8000/recommend

Example Response
[
  {
    "id": "bitcoin",
    "symbol": "btc",
    "current_price": 111535,
    "score": 0.762,
    "market_cap": 2224290696574
  },
  {
    "id": "ethereum",
    "symbol": "eth",
    "current_price": 3210,
    "score": 0.653,
    "market_cap": 454000000000
  }
]