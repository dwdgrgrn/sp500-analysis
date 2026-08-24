import yfinance as yf
import numpy as np

data = yf.Ticker("^GSPC").history("5y")

close_values = data["Close"].values

log_returns = []    # Array of log returns at close of each day

for i in range(close_values.size - 1):
    log_returns.append(np.log(close_values[i+1] / close_values[i]))

mean = np.mean(log_returns)
var = np.var(log_returns)
std = np.sqrt(var)


current_close = close_values[-1]
days_into_future = 365*5
num_of_simulations = 10000

future_close_values = np.empty((num_of_simulations, days_into_future))

random_returns = np.random.normal(mean, std, size=(num_of_simulations, days_into_future))

for i in range(num_of_simulations):
    latest_close = current_close
    for j in range(days_into_future):
        future_close_values[i, j] = latest_close * np.exp(random_returns[i][j])
        latest_close = future_close_values[i, j]

final_close_values = np.sort(future_close_values[:, -1])

confidence_level = 0.995
percentile = 1 - confidence_level

percentile_index = int(percentile * num_of_simulations)

percentile_price = final_close_values[percentile_index]
percentage_difference = ((final_close_values[percentile_index] / current_close) - 1) * 100

print("\n")
print(f"Confidence Level:      {confidence_level * 100}%")
print(f"Simulations:           {num_of_simulations}")
print(f"Days into Future:      {days_into_future}\n")

print(f"Current Close:         {current_close}")
print(f"Simulation Close:      {percentile_price}\n")


print(f"Percentage Difference: {percentage_difference:.2f}%\n")