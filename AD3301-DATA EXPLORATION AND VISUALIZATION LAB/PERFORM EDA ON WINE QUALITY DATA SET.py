import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv("C:/Users/manoj/OneDrive/Documents/DEV LAB/wineQT.csv")

#columns
print(df.columns)

#Summary statistics
print(df.describe())

#unique values
sns.catplot(x='quality', data=df, kind='count')

#Correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
plt.show()
