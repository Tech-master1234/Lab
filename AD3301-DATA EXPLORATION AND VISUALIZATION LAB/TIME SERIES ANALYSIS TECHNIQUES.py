# Import libraries
from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot, lag_plot
from statsmodels.tsa.seasonal import seasonal_decompose

# =======================
# Load the dataset
# =======================
series = read_csv(
    r'datasets\sample_temperature_data.csv',  # make sure path is correct
    header=0,
    index_col=0,
    parse_dates=True
)

# =======================
# Line plot
# =======================
series.plot(title='Time Series Line Plot', figsize=(10, 5))
pyplot.xlabel('Date')
pyplot.ylabel('Temperature (°C)')
pyplot.show()

# =======================
# Histogram & Density
# =======================
fig, axes = pyplot.subplots(2, 1, figsize=(12, 6))

# Histogram
series.plot(kind='hist', bins=20, alpha=0.7, ax=axes[0])
axes[0].set_title('Histogram of Temperature')
axes[0].set_xlabel('Temperature (°C)')
axes[0].set_ylabel('Frequency')

# Density plot
series.plot(kind='kde', ax=axes[1])
axes[1].set_title('Density Plot of Temperature')
axes[1].set_xlabel('Temperature (°C)')
axes[1].set_ylabel('Density')

pyplot.tight_layout()
pyplot.show()

# =======================
# Autocorrelation
# =======================
autocorrelation_plot(series)
pyplot.title('Autocorrelation Plot')
pyplot.xlabel('Lag')
pyplot.ylabel('Autocorrelation')
pyplot.show()

# =======================
# Lag Scatter Plot
# =======================
lag_plot(series)
pyplot.title('Lag Scatter Plot')
pyplot.xlabel('Temperature (t)')
pyplot.ylabel('Temperature (t+1)')
pyplot.show()

# Optional
# =======================
# Seasonal Decomposition (optional, useful in time series)
# =======================
# You can adjust 'period' based on your dataset (e.g., 12 for monthly data, 365 for daily)
decomposition = seasonal_decompose(series, model='additive', period=12)
decomposition.plot()
pyplot.show()
