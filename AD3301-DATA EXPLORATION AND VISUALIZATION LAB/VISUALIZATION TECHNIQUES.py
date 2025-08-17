# STEP 1: Importing libraries and loading Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

# Load the Titanic dataset
data = pd.read_csv("datasets/titanic_train.csv")

# Load the Tips dataset
tips = load_dataset("tips")

# STEP 2: Pie Chart
data['Sex'].value_counts().plot(kind="pie", autopct="%.2f")
plt.title("Distribution of Passengers by Sex")
plt.show()

# STEP 3: Histogram
plt.hist(data['Age'].dropna(), bins=5, color="skyblue", edgecolor="black")
plt.title("Age Distribution (Histogram)")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# STEP 4: Distribution Plot (replacing deprecated distplot)
sns.histplot(data['Age'].dropna(), kde=True, color="purple")
plt.title("Age Distribution with KDE")
plt.show()

# STEP 5: Scatter Plot (tips dataset)
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", style="smoker", palette="Set1")
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

# STEP 6: Boxplot + IQR calculation
Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3 - Q1
Lower_boundary = Q1 - 1.5 * IQR
Upper_boundary = Q3 + 1.5 * IQR

sns.boxplot(x='Pclass', y='Age', data=data)
plt.title("Age Distribution by Passenger Class")
plt.show()

# STEP 7: Bar Plot
sns.barplot(x='Pclass', y='Age', data=data, ci=None, palette="Blues_d")
plt.title("Average Age by Passenger Class")
plt.show()

# Survival Age Distributions
sns.kdeplot(data[data['Survived'] == 0]['Age'].dropna(), color="blue", label="Not Survived")
sns.kdeplot(data[data['Survived'] == 1]['Age'].dropna(), color="orange", label="Survived")
plt.title("Age Distribution by Survival")
plt.legend()
plt.show()


