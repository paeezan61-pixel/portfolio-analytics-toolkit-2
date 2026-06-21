import pandas as pd

def daily_returns(prices):
    return prices.pct_change().dropna()

def sharpe_ratio(returns):
    return (returns.mean() / returns.std()) * (252 ** 0.5)

def max_drawdown(growth):

    running_max = growth.cummax()

    drawdown = (
        growth - running_max
    ) / running_max

    return drawdown.min()

def volatility(returns):
    return returns.std() * (252 ** 0.5)

def cagr(growth):

    years = len(growth) / 252

    return (
        growth.iloc[-1]
        ** (1 / years)
    ) - 1

def correlation_matrix(returns):
    return returns.corr()

