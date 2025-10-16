import pandas as pd
import numpy as np


def rank_assets(df):
    df["volume_ratio"] = df["total_volume"] / df["market_cap"]
    df["score"] = (
        0.5 * df["price_change_percentage_7d_in_currency"].fillna(0)
        + 0.3 * df["volume_ratio"]
        - 0.2 * df["price_change_percentage_24h"].abs()
    )
    df = df.sort_values("score", ascending=False)
    return df[["id", "symbol", "score", "current_price"]].head(10)


