import numpy as np
import pandas as pd

from src.optimization import (
    portfolio_performance,
    random_portfolios,
    efficient_frontier
)


def test_portfolio_performance():

    weights = np.array(
        [0.5, 0.5]
    )

    mean_returns = np.array(
        [0.10, 0.20]
    )

    covariance = np.array(
        [
            [0.01, 0.0],
            [0.0, 0.04]
        ]
    )

    portfolio_return, portfolio_vol = (
        portfolio_performance(
            weights,
            mean_returns,
            covariance
        )
    )

    assert portfolio_return > 0
    assert portfolio_vol > 0


from src.optimization import (
    random_portfolios
)
    
def test_random_portfolios():

    mean_returns = np.array(
        [0.10, 0.20]
    )

    covariance = np.array(
        [
            [0.01, 0.0],
            [0.0, 0.04]
        ]
    )

    results, weights = (
        random_portfolios(
            100,
            mean_returns,
            covariance
        )
    )

    assert len(results) == 100

    assert len(weights) == 100


def test_efficient_frontier():

    returns = pd.DataFrame(
        {
            "A": [0.01, 0.02, 0.03],
            "B": [0.02, 0.01, 0.03]
        }
    )

    results, weights = (
        efficient_frontier(
            returns,
            100
        )
    )

    assert len(results) == 100

    assert len(weights) == 100