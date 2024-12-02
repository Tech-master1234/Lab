import numpy as np
import pandas as pd
from scipy.stats import randint
import pandas as pd
import matplotlib.pyplot as plt
from pandas import set_option
plt.style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn import metrics
import warnings
from sklearn.metrics import classification_report

warnings.filterwarnings("ignore", category=FutureWarning)

BankCreditCard = pd.read_csv("C:/Users/manoj/OneDrive/Documents/AI LAB/BankCreditCard.csv")
print(f'The shape of the dataframe is {BankCreditCard.shape}')
print()
print(BankCreditCard.info())
print()
BankCreditCard.replace(to_replace='?', value=np.NaN, inplace=True)
print(BankCreditCard.describe(include='all'))
print()
print(BankCreditCard['Credit_Amount'].value_counts())
print(BankCreditCard.isnull().sum())

import seaborn as sns
sns.countplot(x='Credit_Amount', data=BankCreditCard, linewidth=3)
plt.show()

BankCreditCard[['Customer ID', 'Credit_Amount', 'Gender', 'Academic_Qualification', 'Marital', 'Age_Years', 'Jan_Bill_Amount', 'Feb_Bill_Amount']].hist(bins=50, figsize=(15, 8))
plt.show()

BankCreditCard['Credit_Amount'].fillna(BankCreditCard['Credit_Amount'].mode()[0], inplace=True)
BankCreditCard['Jan_Bill_Amount'].fillna(BankCreditCard['Jan_Bill_Amount'].mode()[0], inplace=True)

X = BankCreditCard.drop(['Marital'], axis=1)
y = BankCreditCard['Marital']

X = X[['Repayment_Status_Jan', 'Repayment_Status_Feb', 'Repayment_Status_March', 'Repayment_Status_April', 'Repayment_Status_May']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

NB_classifier = GaussianNB()
NB_classifier.fit(X_train, y_train)
y_predict = NB_classifier.predict(X_test)

cm = confusion_matrix(y_test, y_predict)
sns.heatmap(cm, annot=True, cmap='Blues')
print(classification_report(y_test, y_predict))
