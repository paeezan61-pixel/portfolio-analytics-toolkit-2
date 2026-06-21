def portfolio_returns(returns, weights):

    portfolio_return = (
        returns * weights
    ).sum(axis=1)

    return portfolio_return