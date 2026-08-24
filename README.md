# sp500-analysis
A Monte Carlo simulation estimating the probability of the S&P 500 falling below a given price over a chosen time period.

## Libraries used
- yfinance
- numpy

## Setup
- Used yfinance library to retrieve an array of values from the S&P 500 stock market.
- Extracted the close values for each day for the last 5 years.

## Distribution of the historical data
- The best way to calculate the difference between the close value day-to-day is by applying log to the close value of a given day, divided by the close value for the previous day.
- Created an array dating back 5 years.
- Calculated the mean and variance which will be used later on to simulate values.

## Simulating values
- Added variables for the "days into the future" and "number of simulations" and also a "current close" variable referring to today's close price.
- Initially I created a for loop that generates new values from the normal distribution (with the mean and standard deviation as parameters).
- Found a more efficient way which involved creating a 2D array of values from the normal distribution and accessing the array in the for loop; this nearly halved the processing time.
- Extracted the close value of the last day from each of the simulations and sorted them in ascending order.

## Conclusion
- To find the percentile price, I simply index the percentile multiplied by the number of simulations from the array.
- This gives the price at which there is an "x" confidence level that it will not fall below that value.
- Finally calculated the percentage change from the current close price to give a comparison

## Findings
- The more days into the future I ran the simulation, the higher the percentile price was calculated. This is expected as there is an uptrend to the S&P 500 stock market.
- There is a significant jump in the percentage difference between today's price and the final close price between confidence levels: 99.5% and 95%. One simulation I ran had a jump from a loss of ~30% to a loss of only ~16% respectively. A pattern I noticed from these two percentages was that the more days into the future the simulations ran, the larger the difference was between the two percentages.

## Limitations
- The simulation ran assumes that the close price difference after each day is a normal distribution, which is unlikely to be the case.
- The simulation doesn't take into account any factors that could affect it in the future and is purely based on the average of historical prices.
