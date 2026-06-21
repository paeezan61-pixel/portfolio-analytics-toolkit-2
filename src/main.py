import matplotlib.pyplot as plt

from data_loader import download_prices

from metrics import (
    daily_returns,
    sharpe_ratio,
    max_drawdown,
    volatility,
    cagr
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
portfolio_sr = sharpe_ratio(
    portfolio_ret
)

portfolio_vol = volatility(
    portfolio_ret
)

portfolio_cagr = cagr(
    growth
)

print("Portfolio Sharpe Ratio:")
print(portfolio_sr)

print("\nAnnualized Volatility:")
print(f"{portfolio_vol:.2%}")

print("\nMaximum Drawdown:")
print(f"{mdd:.2%}")

print("\nCAGR:")
print(f"{portfolio_cagr:.2%}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
growth.plot()
plt.title("Portfolio Growth")

plt.subplot(1, 2, 2)
plt.pie(
    weights,
    labels=tickers,
    autopct="%1.1f%%"
)
plt.title("Portfolio Allocation")

plt.tight_layout()
plt.show()