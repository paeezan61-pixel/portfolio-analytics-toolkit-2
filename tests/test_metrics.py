import pytest
import pandas as pd

from src.metrics import (
    daily_returns,
    sharpe_ratio,
    volatility,
    max_drawdown,
    cagr,
    correlation_matrix,
    beta,
    alpha,
    tracking_error,
    information_ratio
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

    def test_tracking_error():

        portfolio = pd.Series(
        [0.02, 0.01, -0.01, 0.03]
    )

        benchmark = pd.Series(
        [0.01, 0.01, -0.02, 0.02]
    )

        result = tracking_error(
        portfolio,
        benchmark
    )

        assert result > 0


def test_information_ratio():

    portfolio = pd.Series(
        [0.02, 0.01, -0.01, 0.03]
    )

    benchmark = pd.Series(
        [0.01, 0.01, -0.02, 0.02]
    )

    result = information_ratio(
        portfolio,
        benchmark
    )

    assert result > 0

def test_correlation_matrix():

    returns = pd.DataFrame(
        {
            "A": [0.01, 0.02, 0.03],
            "B": [0.01, 0.02, 0.03]
        }
    )

    corr = correlation_matrix(
        returns
    )

    assert corr.loc["A", "B"] == 1.0



def test_beta_positive():

    portfolio = pd.Series(
        [0.02, 0.01, -0.01, 0.03]
    )

    benchmark = pd.Series(
        [0.01, 0.01, -0.02, 0.02]
    )

    result = beta(
        portfolio,
        benchmark
    )

    assert result > 0


