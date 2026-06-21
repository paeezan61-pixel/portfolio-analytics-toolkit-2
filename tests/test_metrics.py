import pandas as pd

from src.metrics import daily_returns


def test_daily_returns():

    prices = pd.Series(
        [100, 110, 121]
    )

    returns = daily_returns(
        prices
    )

    expected = pd.Series(
        [0.10, 0.10],
        index=[1, 2]
    )

    pd.testing.assert_series_equal(
        returns,
        expected
    )