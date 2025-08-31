import numpy as np
import pandas as pd


def evaluate_strategy(signal: pd.Series, returns_strategy: pd.Series):
    equity_curve = returns_strategy.cumsum().apply(np.exp)
    num_months = equity_curve.index.to_period("M").nunique()
    num_years = num_months / 12
    total_return = equity_curve.iloc[-1].item() / equity_curve.iloc[0].item() - 1
    annualized_return = (1 + total_return) ** (1 / num_years) - 1
    number_of_trades = signal.diff().abs().sum().item()
    gross_profit = returns_strategy[returns_strategy > 0].sum()
    gross_loss = -returns_strategy[returns_strategy < 0].sum()
    profit_factor = (
        (gross_profit / gross_loss).item() if gross_loss != 0 else np.nan.item()
    )

    print(f"  Total Return: {total_return:.2%}")
    print(f"  Annualized Return: {annualized_return:.2%}")
    print(f"  Profit factor: {profit_factor:.4f}")
    print(f"  Number of trades: {number_of_trades:.0f}")

    return {
        "equity_curve": equity_curve,
        "total_return": total_return,
        "profit_factor": profit_factor,
        "annualized_return": annualized_return,
        "number_of_trades": number_of_trades,
    }
