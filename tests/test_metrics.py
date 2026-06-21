import pytest
import pandas as pd

from src.metrics import (
    daily_returns,
    beta,
    alpha,
    volatility,
    cagr,
    max_drawdown
)


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


def test_beta():

    portfolio = pd.Series(
        [0.02, 0.01, -0.01, 0.03]
    )

    benchmark = pd.Series(
        [0.01, 0.01, -0.005, 0.02]
    )

    result = beta(
        portfolio,
        benchmark
    )

    assert result > 0


def test_alpha():

    result = alpha(
        0.12,
        0.08,
        1
    )

    assert result == pytest.approx(0.04)


def test_volatility():

    returns = pd.Series(
        [0.01, -0.01, 0.02, -0.02]
    )

    result = volatility(
        returns
    )

    assert result > 0


def test_cagr():

    growth = pd.Series(
        [1.0, 1.1, 1.2]
    )

    result = cagr(
        growth
    )

    assert result > 0


def test_max_drawdown():

    growth = pd.Series(
        [1.0, 1.2, 1.1, 1.3]
    )

    result = max_drawdown(
        growth
    )

    assert result < 0