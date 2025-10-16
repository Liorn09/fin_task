from dotenv import load_dotenv
import os
import requests
import pandas as pd
import numpy as np
load_dotenv()


API_KEY = os.getenv("COINGEKO_KEY")

def fetch_market_data():
    headers = {
        "Accept": "application/json",
        "X-CoinGecko-Api-Key": API_KEY
    }
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h,7d"
    }
    data = requests.get(url, params=params, headers=headers).json()
    # df = pd.DataFrame(data)
    return data
    return df[["id", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h", "price_change_percentage_7d_in_currency"]]
