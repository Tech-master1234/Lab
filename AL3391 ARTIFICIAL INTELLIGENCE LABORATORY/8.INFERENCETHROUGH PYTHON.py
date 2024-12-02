import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

data = pd.read_csv('C:/Users/manoj/OneDrive/Documents/AI LAB/database.csv')
cols_of_interest = ['AccidentDate/Time', 'AccidentState', 'PipelineLocation', 'LiquidType', 'NetLoss(Barrels)', 'AllCosts']
data = data[cols_of_interest]
data_summary = print(data[['AllCosts', 'NetLoss(Barrels)']])
data['AllCosts'] = data['AllCosts'] / 1000000

sns.boxplot(data['AllCosts'])
plt.title('Costs of Accident')
plt.show()
plt.close()

sns.boxplot(data['NetLoss(Barrels)'])
plt.title('Net Loss (Barrels)')
plt.show()

data['AccidentDate/Time'] = pd.to_datetime(data['AccidentDate/Time'])
total_timespan = np.max(data['AccidentDate/Time']) - np.min(data['AccidentDate/Time'])
total_time_hour = (total_timespan.days * 24 + total_timespan.seconds / 3600)
total_time_month = (total_timespan.days + total_timespan.seconds / (3600 * 24)) * 12 / 365
Imda_h = len(data) / total_time_hour
Imda_m = len(data) / total_time_month
print('Estimated no. of Accident per hour: {}'.format(Imda_h))
print('Estimated no. of Accident per month: {}'.format(Imda_m))

X = {}
for i in range(66):
    X[i] = math.pow(2.71828, -1 * 33) * math.pow(33, i) / math.factorial(i)

p_Poission = pd.DataFrame(X.items(), columns=['X', 'PX'])
fig = plt.subplots(figsize=(15, 10))
plt.plot(p_Poission['X'], p_Poission['PX'], marker='.', color='purple', linestyle='solid')
plt.xlabel('Number of Accident Per Month (n)')
plt.ylabel('P(X<=n)')
plt.title('Probability Mass Function')
plt.show()
plt.close()

def cdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y

np.random.seed(42)
sample_Poission = np.random.poisson(33, 10000)
x, y = cdf(sample_Poission)
fig = plt.subplots(figsize=(15, 10))
plt.plot(x, y, marker='', alpha=0.5, color='purple', linestyle='solid')
plt.xlabel('Number of Accident Per Month (n)')
plt.ylabel('P(X<=n)')
plt.title('Cumulative Distribution Function')
plt.show()
