import matplotlib.pyplot as plt

from data_loader import download_prices

from metrics import (
    daily_returns,
    sharpe_ratio,
    max_drawdown
)

from portfolio import (
    portfolio_returns,
    portfolio_growth
)

tickers = ["AAPL", "MSFT", "SPY"]

weights = [0.4, 0.3, 0.3]

prices = download_prices(tickers)

returns = daily_returns(prices)

portfolio_ret = portfolio_returns(
    returns,
    weights
)

portfolio_sr = sharpe_ratio(
    portfolio_ret
)

growth = portfolio_growth(
    portfolio_ret
)

mdd = max_drawdown(
    growth
)

print("Portfolio Sharpe Ratio:")
print(portfolio_sr)

print("\nMaximum Drawdown:")
print(f"{mdd:.2%}")

growth.plot()

plt.title("Portfolio Growth")
plt.show()