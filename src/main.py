import matplotlib.pyplot as plt

from data_loader import download_prices

from metrics import (
    daily_returns,
    sharpe_ratio,
    max_drawdown,
    volatility,
    cagr,
    correlation_matrix
)

from portfolio import (
    portfolio_returns,
    portfolio_growth
)

tickers = ["AAPL", "MSFT", "SPY"]

benchmark = "SPY"

weights = [0.4, 0.3, 0.3]


prices = download_prices(tickers)
benchmark_prices = download_prices(
    benchmark
)

benchmark_prices = benchmark_prices.squeeze()

returns = daily_returns(prices)

benchmark_returns = daily_returns(
    benchmark_prices
)

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

benchmark_growth = portfolio_growth(
    benchmark_returns
)

mdd = max_drawdown(
    growth
)


portfolio_vol = volatility(
    portfolio_ret
)

portfolio_cagr = cagr(
    growth
)


benchmark_cagr = cagr(
    benchmark_growth
)

corr = correlation_matrix(
    returns
)

print("Portfolio Sharpe Ratio:")
print(portfolio_sr)

print("\nAnnualized Volatility:")
print(f"{portfolio_vol:.2%}")

print("\nMaximum Drawdown:")
print(f"{mdd:.2%}")

print("\nPortfolio CAGR:")
print(f"{portfolio_cagr:.2%}")

print("\nCorrelation Matrix:")
print(corr)

print("\nBenchmark CAGR:")
print(f"{benchmark_cagr:.2%}")

plt.figure(figsize=(6, 5))

plt.imshow(corr)

plt.savefig(
    "docs/images/correlation-heatmap.png",
    bbox_inches="tight"
)

plt.colorbar()

plt.xticks(
    range(len(corr.columns)),
    corr.columns
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

plt.title("Correlation Matrix")

plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

plt.plot(
    growth.index,
    growth,
    label="Portfolio"
)

plt.plot(
    benchmark_growth.index,
    benchmark_growth,
    label="SPY"
)

plt.title("Portfolio vs Benchmark")
plt.legend()

plt.savefig(
    "docs/images/portfolio-vs-benchmark.png",
    bbox_inches="tight"
)

plt.subplot(1, 2, 2)
plt.pie(
    weights,
    labels=tickers,
    autopct="%1.1f%%"
)

plt.savefig(
    "docs/images/allocation-chart.png",
    bbox_inches="tight"
)

plt.title("Portfolio Allocation")

plt.tight_layout()
plt.show()