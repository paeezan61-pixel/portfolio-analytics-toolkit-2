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