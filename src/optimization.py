import numpy as np


def portfolio_performance(
    weights,
    mean_returns,
    covariance_matrix
):
    portfolio_return = np.sum(
        mean_returns * weights
    ) * 252

    portfolio_volatility = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                covariance_matrix * 252,
                weights
            )
        )
    )

    return (
        portfolio_return,
        portfolio_volatility
    )


def sharpe_ratio_portfolio(
    portfolio_return,
    portfolio_volatility,
    risk_free_rate=0
):
    return (
        portfolio_return
        - risk_free_rate
    ) / portfolio_volatility


import numpy as np


def random_portfolios(
    num_portfolios,
    mean_returns,
    covariance_matrix,
    risk_free_rate=0
):
    results = []

    weights_record = []

    num_assets = len(mean_returns)

    for _ in range(num_portfolios):

        weights = np.random.random(
            num_assets
        )

        weights /= np.sum(weights)

        portfolio_return, portfolio_volatility = (
            portfolio_performance(
                weights,
                mean_returns,
                covariance_matrix
            )
        )

        sharpe = sharpe_ratio_portfolio(
            portfolio_return,
            portfolio_volatility,
            risk_free_rate
        )

        results.append(
            [
                portfolio_return,
                portfolio_volatility,
                sharpe
            ]
        )

        weights_record.append(weights)

    return (
        np.array(results),
        weights_record
    )


def efficient_frontier(
    returns,
    num_portfolios=5000,
    risk_free_rate=0
):
    mean_returns = returns.mean()

    covariance_matrix = returns.cov()

    results, weights = random_portfolios(
        num_portfolios,
        mean_returns,
        covariance_matrix,
        risk_free_rate
    )

    return results, weights