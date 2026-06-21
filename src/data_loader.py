import yfinance as yf


def download_prices(ticker, period="1y"):
    data = yf.download(ticker, period=period)
    return data