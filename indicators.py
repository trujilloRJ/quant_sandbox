import pandas as pd


def get_sma(data: pd.DataFrame, window: int, col_name="Close") -> pd.Series:
    return data[col_name].rolling(window=window).mean()


def get_std(data: pd.DataFrame, window: int, col_name="Close") -> pd.Series:
    return data[col_name].rolling(window=window).std()
