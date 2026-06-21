from data_loader import download_prices
from metrics import daily_returns

data = download_prices("AAPL")

returns = daily_returns(data["Close"])

print(returns.tail())
