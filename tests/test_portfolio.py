import pandas as pd

from src.portfolio import portfolio_returns


def test_portfolio_returns():

    returns = pd.DataFrame(
        {
            "AAPL": [0.10],
            "MSFT": [0.20]
        }
    )

    weights = [0.5, 0.5]

    result = portfolio_returns(
        returns,
        weights
    )

    expected = pd.Series(
        [0.15]
    )

    pd.testing.assert_series_equal(
        result,
        expected,
        check_names=False
    )