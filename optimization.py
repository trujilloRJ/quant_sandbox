import pandas as pd
from tqdm.contrib import itertools
import numpy as np


def optimize_strategy_brute_force(
    data: pd.DataFrame, strategy_fn: callable, params_space: dict
):
    strategy_df = pd.DataFrame(index=data.index)
    profit_factors = {}
    for params in itertools.product(*params_space.values()):
        params = [p.item() if isinstance(p, np.generic) else p for p in params]
        param_dict = dict(zip(params_space.keys(), params))
        strategy_df = strategy_fn(data, **param_dict)
        returns_strategy = (
            data.loc[strategy_df.index, "returns_log"] * strategy_df["signal"]
        )
        gross_profit = returns_strategy[returns_strategy > 0].sum()
        gross_loss = -returns_strategy[returns_strategy < 0].sum()

        key = tuple(params)
        profit_factors[key] = (gross_profit / gross_loss).item()

    profit_factors = dict(
        sorted(profit_factors.items(), key=lambda x: x[1], reverse=True)
    )
    return profit_factors
