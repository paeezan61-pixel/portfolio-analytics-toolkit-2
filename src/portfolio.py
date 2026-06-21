def portfolio_returns(returns, weights):

    portfolio_return = (
        returns * weights
    ).sum(axis=1)

    return portfolio_return


def portfolio_growth(portfolio_returns):

    growth = (
        1 + portfolio_returns
    ).cumprod()

    return growth