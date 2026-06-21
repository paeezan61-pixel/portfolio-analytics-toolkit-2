from metrics import cagr

portfolio_start = 10000
portfolio_end = 15000
years = 3

result = cagr(portfolio_start, portfolio_end, years)

print(f"CAGR: {result:.2%}")