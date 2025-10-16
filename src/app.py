from fastapi import FastAPI
from pydantic import BaseModel
from data_fetcher import fetch_market_data
from model import rank_assets


# define the payload structure here
class AssetRequest(BaseModel):
    currency: str = "usd"
    per_page: int = 100
    page: int = 1


app = FastAPI()


@app.post("/top-assets")
def get_top_assets(details: AssetRequest):
    currency = details.currency
    per_page = details.per_page
    page = details.page
    df = fetch_market_data(currency, per_page, page)
    if df.empty:
        return {"error": "Failed to fetch market data"}
    top_assets = rank_assets(df)
    return top_assets.to_dict(orient="records")
