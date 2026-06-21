from data_loader import download_prices
from metrics import daily_returns, sharpe_ratio
from portfolio import portfolio_returns

tickers = ["AAPL", "MSFT", "SPY"]

weights = [0.4, 0.3, 0.3]

prices = download_prices(tickers)

returns = daily_returns(prices)

portfolio_ret = portfolio_returns(
    returns,
    weights
)

portfolio_sr = sharpe_ratio(portfolio_ret)

print("Portfolio Sharpe Ratio:")
print(portfolio_sr)