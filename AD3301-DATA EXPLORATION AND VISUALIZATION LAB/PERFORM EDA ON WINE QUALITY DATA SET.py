import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv("datasets/wineQT.csv")

#columns
print(df.columns)

#Summary statistics
print(df.describe())

#unique values
# Same Color
sns.catplot(x='quality', data=df, kind='count')

'''
Auto Colors
sns.catplot(
    x="quality",
    data=df,
    kind="count",
    palette="Set2"   # Try "Set1", "Paired", "viridis", etc.
)
'''
'''
# Custom Colors
custom_colors = {
    "3": "blue",
    "4": "orange",
    "5": "green",
    "6": "red",
    "7": "violet",
    "8": "brown"
}

sns.catplot(x="quality",data=df,kind="count",palette=custom_colors)
'''

#Correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), color = 'k', annot=True)
plt.show()
