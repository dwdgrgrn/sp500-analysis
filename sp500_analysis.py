import yfinance as yf
import numpy as np

data = yf.Ticker("^GSPC").history("5y")

close_values = data["Close"].values

log_returns = []    # Array of log returns at the end of each day

for i in range(close_values.size - 1):
    log_returns.append(np.log(close_values[i+1] / close_values[i]))

print(np.mean(log_returns))
print(np.var(log_returns))