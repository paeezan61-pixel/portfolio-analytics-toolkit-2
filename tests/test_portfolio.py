import pytest
import pandas as pd

from src.portfolio import (
    portfolio_returns,
    portfolio_growth
)


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

def test_portfolio_growth():

    returns = pd.Series(
        [0.10, 0.10]
    )

    growth = portfolio_growth(
        returns
    )

    assert growth.iloc[-1] == pytest.approx(
        1.21
    )


