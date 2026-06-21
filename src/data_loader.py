import yfinance as yf


def download_prices(tickers, period="1y"):
    data = yf.download(
        tickers,
        period=period,
        auto_adjust=True
    )

    return data["Close"]