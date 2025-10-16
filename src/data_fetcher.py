from dotenv import load_dotenv
import os
import requests
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
load_dotenv()


API_KEY = os.getenv("COINGEKO_KEY")


def fetch_market_data(currency="usd", per_page=100, page=1):
    # define headers and parameters for the API request
    headers = {
        "Accept": "application/json",
        "X-CoinGecko-Api-Key": API_KEY
    }
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page,
        "sparkline": "false",
        "price_change_percentage": "24h,7d"
    }
    # fetch data from the API and convert to a pandas DataFrame
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.3,
                    status_forcelist=[429, 500,
                                      502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    try:
        response = session.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    df = pd.DataFrame(data)
    return df[["id", "symbol", "current_price", "market_cap", "total_volume",
               "price_change_percentage_24h",
               "price_change_percentage_7d_in_currency"]]
