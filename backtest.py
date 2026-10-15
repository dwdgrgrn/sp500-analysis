import yfinance as yf
import numpy as np

data = yf.Ticker("^GSPC").history("20y")

close_values = data["Close"].values

log_returns = []    # Array of log returns at close of each day

for i in range(close_values.size - 1):
    log_returns.append(np.log(close_values[i+1] / close_values[i]))

window = 252 * 5    # about 5 years of trading days

confidence_level = 0.995
percentile = 1 - confidence_level
num_of_simulations = 10000

test_days = len(log_returns) - window

normal_breaches = 0         # Where it falls below the price (simulated)
historical_breaches = 0     # Where it falls below the price (historical)

for day in range(window, len(log_returns)):
    past_returns = log_returns[day - window:day]

    mean = np.mean(past_returns)
    var = np.var(past_returns)
    std = np.sqrt(var)

    current_close = close_values[day]
    actual_close = close_values[day+1]

    random_returns = np.random.normal(mean, std, num_of_simulations)
    simulated_closes = np.sort(current_close * np.exp(random_returns))
    percentile_index = int(percentile * num_of_simulations)
    simulated_price = simulated_closes[percentile_index]

    sorted_returns = np.sort(past_returns)
    historical_index = int(percentile * window)
    historical_price = current_close * np.exp(sorted_returns[historical_index])

    if actual_close < simulated_price:
        normal_breaches += 1
    if actual_close < historical_price:
        historical_breaches += 1

expected = percentile * test_days
std_expected = np.sqrt(test_days * percentile * confidence_level)

print("\n")
print(f"Confidence Level:        {confidence_level * 100}%")
print(f"Test Days:               {test_days}")
print(f"Expected Breaches:       {expected:.0f} ({percentile * 100:.2f}%)\n")

print(f"Monte Carlo Breaches:    {normal_breaches} ({normal_breaches / test_days * 100:.2f}%)")
print(f"Std Devs from Expected:  {(normal_breaches - expected) / std_expected:.2f}\n")

print(f"Historical Breaches:     {historical_breaches} ({historical_breaches / test_days * 100:.2f}%)")
print(f"Std Devs from Expected:  {(historical_breaches - expected) / std_expected:.2f}\n")


