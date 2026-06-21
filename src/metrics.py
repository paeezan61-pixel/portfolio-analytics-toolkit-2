import pandas as pd


def daily_returns(prices):
    return prices.pct_change().dropna()


def sharpe_ratio(returns):
    return (returns.mean() / returns.std()) * (252 ** 0.5)