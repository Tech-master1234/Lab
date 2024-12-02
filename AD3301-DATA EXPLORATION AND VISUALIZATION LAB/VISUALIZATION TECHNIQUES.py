# STEP 1: Importing libraries and loading Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

# Load the Titanic dataset
data = pd.read_csv("C:/Users/manoj/OneDrive/Documents/DEV LAB/titanic_train.csv")

# Load the Tips dataset
tips = load_dataset("tips")

# STEP 2: Pie Chart
data['Sex'].value_counts().plot(kind="pie", autopct="%.2f")
plt.show()

# STEP 3: Histogram
plt.hist(data['Age'], bins=5)
plt.show()

# STEP 4: Distplot
sns.distplot(data['Age'])
plt.show()

# STEP 5: Boxplot
# Calculate IQR
Q1 = data['Age'].quantile(0.25)
Q3 = data['Age'].quantile(0.75)
IQR = Q3 - Q1

#Calculate lower and upper bounds
Lower_boundary = Q1 - 1.5 * IQR
Upper_boundary = Q3 + 1.5 * IQR

# STEP 6: Bar Plot
sns.barplot(x='Pclass', y='Age', data=data)
plt.show()

#Distplot
sns.distplot(data[data['Survived'] == 0]['Age'], hist=False, color="blue") 
sns.distplot(data[data['Survived'] == 1]['Age'], hist=False, color="orange")
plt.show()
