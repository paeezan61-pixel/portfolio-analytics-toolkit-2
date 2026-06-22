import matplotlib.pyplot as plt

from data_loader import download_prices

from metrics import (
    daily_returns,
    sharpe_ratio,
    max_drawdown,
    volatility,
    cagr,
    correlation_matrix,
    beta,
    alpha,
    tracking_error,
    information_ratio
)

from portfolio import (
    portfolio_returns,
    portfolio_growth
)


from optimization import (
    efficient_frontier
)
# -----------------------------------
# Portfolio Setup
# -----------------------------------



tickers = ["AAPL", "MSFT", "SPY"]

benchmark = "SPY"

weights = [0.4, 0.3, 0.3]

# -----------------------------------
# Download Data
# -----------------------------------

prices = download_prices(tickers)

benchmark_prices = download_prices(
    benchmark
)

benchmark_prices = benchmark_prices.squeeze()

# -----------------------------------
# Returns
# -----------------------------------

returns = daily_returns(prices)

benchmark_returns = daily_returns(
    benchmark_prices
)

portfolio_ret = portfolio_returns(
    returns,
    weights
)

# -----------------------------------
# Growth Curves
# -----------------------------------

growth = portfolio_growth(
    portfolio_ret
)

benchmark_growth = portfolio_growth(
    benchmark_returns
)

# -----------------------------------
# Core Metrics
# -----------------------------------

portfolio_sr = sharpe_ratio(
    portfolio_ret
)

portfolio_vol = volatility(
    portfolio_ret
)

mdd = max_drawdown(
    growth
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


frontier_results, frontier_weights = (
    efficient_frontier(
        returns,
        5000
    )
)
# -----------------------------------
# Benchmark Analytics
# -----------------------------------

portfolio_beta = beta(
    portfolio_ret,
    benchmark_returns
)

portfolio_alpha = alpha(
    portfolio_cagr,
    benchmark_cagr,
    portfolio_beta
)

portfolio_tracking_error = tracking_error(
    portfolio_ret,
    benchmark_returns
)

portfolio_information_ratio = (
    information_ratio(
        portfolio_ret,
        benchmark_returns
    )
)

# -----------------------------------
# Console Output
# -----------------------------------

print("Portfolio Sharpe Ratio:")
print(f"{portfolio_sr:.2f}")

print("\nAnnualized Volatility:")
print(f"{portfolio_vol:.2%}")

print("\nMaximum Drawdown:")
print(f"{mdd:.2%}")

print("\nPortfolio CAGR:")
print(f"{portfolio_cagr:.2%}")

print("\nBenchmark CAGR:")
print(f"{benchmark_cagr:.2%}")

print("\nPortfolio Beta:")
print(f"{portfolio_beta:.2f}")

print("\nPortfolio Alpha:")
print(f"{portfolio_alpha:.2%}")

print("\nTracking Error:")
print(f"{portfolio_tracking_error:.2%}")

print("\nInformation Ratio:")
print(f"{portfolio_information_ratio:.2f}")

print("\nCorrelation Matrix:")
print(corr)

# -----------------------------------
# Correlation Heatmap
# -----------------------------------

plt.figure(figsize=(6, 5))

plt.imshow(corr)

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

plt.savefig(
    "docs/images/correlation-heatmap.png",
    bbox_inches="tight"
)

plt.show()

# -----------------------------------
# Portfolio vs Benchmark
# -----------------------------------

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

# -----------------------------------
# Asset Allocation Pie Chart
# -----------------------------------

plt.subplot(1, 2, 2)

plt.pie(
    weights,
    labels=tickers,
    autopct="%1.1f%%"
)

plt.title("Portfolio Allocation")

plt.savefig(
    "docs/images/allocation-chart.png",
    bbox_inches="tight"
)

plt.tight_layout()

plt.show()

plt.figure(figsize=(8, 6))

plt.scatter(
    frontier_results[:, 1],
    frontier_results[:, 0],
    c=frontier_results[:, 2]
)

plt.xlabel("Volatility")

plt.ylabel("Return")

plt.title(
    "Efficient Frontier"
)

plt.colorbar(
    label="Sharpe Ratio"
)

plt.savefig(
    "docs/images/efficient-frontier.png",
    bbox_inches="tight"
)

plt.show()