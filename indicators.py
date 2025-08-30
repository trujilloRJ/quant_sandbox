import pandas as pd


def get_sma(data: pd.DataFrame, window: int) -> pd.Series:
    return data["Close"].rolling(window=window).mean()
