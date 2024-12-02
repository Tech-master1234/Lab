from pandas import read_csv
from matplotlib import pyplot

series = read_csv('sample_temperature_data.csv', header=0, index_col=0, parse_dates=True)

#line plot
series.plot()
pyplot.title('Time Series Line Plot')
pyplot.xlabel('Date')
pyplot.ylabel('Temperature (°C)')
pyplot.show()

pyplot.figure(figsize=(12, 6))
pyplot.subplot(2, 1, 1)
series.hist()
pyplot.title('Histogram of Temperature')
pyplot.xlabel('Temperature (°C)')
pyplot.ylabel('Frequency')

pyplot.subplot(2, 1, 2)
series.plot(kind='kde')
pyplot.title('Density Plot of Temperature')
pyplot.xlabel('Temperature (°C)')
pyplot.ylabel('Density')
pyplot.tight_layout()
pyplot.show()

from pandas.plotting import autocorrelation_plot

autocorrelation_plot(series)
pyplot.title('Autocorrelation Plot')
pyplot.xlabel('Lag')
pyplot.ylabel('Autocorrelation')
pyplot.show()

from pandas.plotting import lag_plot

lag_plot(series)
pyplot.title('Lag Scatter Plot')
pyplot.xlabel('Temperature (t)')
pyplot.ylabel('Temperature (t+1)')
pyplot.show()
