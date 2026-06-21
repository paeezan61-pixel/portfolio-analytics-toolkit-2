from data_loader import download_prices

data = download_prices("AAPL")

print(data.tail())