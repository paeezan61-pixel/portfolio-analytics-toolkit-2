import numpy as np

def cagr(beginning, ending, years):
    return (ending / beginning) ** (1 / years) - 1

def sharpe_ratio(returns, risk_free_rate=0.02):
    excess_returns = np.mean(returns) - risk_free_rate
    return excess_returns / np.std(returns)

def max_drawdown(values):
    peak = values[0]
    max_dd = 0

    for value in values:
        if value > peak:
            peak = value

        dd = (peak - value) / peak

        if dd > max_dd:
            max_dd = dd

    return max_dd