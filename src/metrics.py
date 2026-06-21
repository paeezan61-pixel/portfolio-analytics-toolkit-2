import pandas as pd


def daily_returns(prices):
    return prices.pct_change().dropna()