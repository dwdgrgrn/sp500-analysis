import yfinance as yf
import numpy as np

data = yf.Ticker("^GSPC").history("5y")

close_values = data["Close"].values

log_returns = []    # Array of log returns at the end of each day

for i in range(close_values.size - 1):
    log_returns.append(np.log(close_values[i+1] / close_values[i]))

mean = np.mean(log_returns)
var = np.var(log_returns)
std = np.sqrt(var)


current_close = close_values[-1]
days_into_future = 365
num_of_simulations = 10000

future_close_values = np.empty((num_of_simulations, days_into_future))

for i in range(num_of_simulations):
    latest_close = current_close
    for j in range(days_into_future):
        future_close_values[i, j] = latest_close * np.exp(np.random.normal(mean, std))
        latest_close = future_close_values[i, j]

print(np.sort(future_close_values[-1])[0])