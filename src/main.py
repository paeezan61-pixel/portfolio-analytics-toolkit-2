from data_loader import download_prices
from metrics import daily_returns, sharpe_ratio

data = download_prices("AAPL")

returns = daily_returns(data["Close"])

print("Latest Returns:")
print(returns.tail())

print("\nSharpe Ratio:")
print(sharpe_ratio(returns))