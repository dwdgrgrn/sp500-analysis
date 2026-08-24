import yfinance as yf

data = yf.Ticker("^GSPC").history("ytd")

print(data.head())