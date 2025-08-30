import numpy as np
import yfinance
import pandas as pd


def fetch_data(
    ticker_symbol: str, start_date: str, end_date: str, interval: str
) -> pd.DataFrame:
    try:
        data = yfinance.download(
            ticker_symbol, start=start_date, end=end_date, interval=interval
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # dropping multi-index if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    return data


def get_equity_curve_buy_and_hold(data: pd.DataFrame) -> pd.DataFrame:
    data.loc[:, "returns_log"] = np.log(data.Close / data.Close.shift(1))
    data.loc[:, "equity_0"] = data.returns_log.cumsum().apply(np.exp)
    return data.dropna()
