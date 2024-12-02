import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import jaccard_score, confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit

# Linear Regression
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print(f"intercept: {new_model.intercept_}")
print(f"slope: {new_model.coef_}")

y_pred = model.predict(x)
print(f"predicted response:\n{y_pred}")

y_pred = model.intercept_ + model.coef_ * x
print(f"predicted response:\n{y_pred}")

x_new = np.arange(5).reshape((-1, 1))
print("XNEW", x_new)
y_new = model.predict(x_new)
print("Ynew", y_new)

# Logistic Regression
disease_df = pd.read_csv("C:/Users/manoj/OneDrive/Documents/AI LAB/logistic.csv")
disease_df.drop(['education'], inplace=True, axis=1)
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)

disease_df.dropna(axis=0, inplace=True)

X = np.asarray(disease_df[['age', 'Sex_male', 'cigsPerDay', 'totChol', 'sysBP', 'glucose']])
y = np.asarray(disease_df['TenYearCHD'])

X = StandardScaler().fit(X).transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print('Accuracy of the model in jaccard similarity score is = ', jaccard_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
conf_matrix = pd.DataFrame(data=cm, columns=['Predicted:0', 'Predicted:1'], index=['Actual:0', 'Actual:1'])

plt.figure(figsize=(8, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Greens")
plt.show()

print('The details for confusion matrix is =')
print(classification_report(y_test, y_pred))

# SVM Based Prediction Models
signals = pd.read_csv("C:/Users/manoj/OneDrive/Documents/AI LAB/DS1_signals.csv", header=None)
labels = pd.read_csv("C:/Users/manoj/OneDrive/Documents/AI LAB/DS1_labels.csv", header=None)

joined_data = signals.join(labels, rsuffix="_signals", lsuffix="_labels")
joined_data.columns = [i for i in range(180)] + ['class']

print("Top 10 highly positively correlated features:")
print(joined_data.corr()['class'].sort_values(ascending=False).head(10))
print("Top 10 highly negatively correlated features:")
print(joined_data.corr()['class'].sort_values().head(10))

# Visualizing the data
sns.pairplot(joined_data[[79, 80, 78, 77, 'class']], hue='class', diag_kind='kde')
plt.show()

split1 = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split1.split(joined_data, joined_data['class']):
    strat_train_set = joined_data.loc[train_index]
    strat_test_set = joined_data.loc[test_index]

strat_features_train = strat_train_set.drop('class', axis=1)
labels_train = strat_train_set['class']
scaler = StandardScaler()
std_features_train = scaler.fit_transform(strat_features_train)

svc_param_grid = {'C': [10], 'gamma': [0.1, 1, 10]}
svc = SVC(kernel='rbf', decision_function_shape='ovo', random_state=42, max_iter=500)
svc_grid_search = GridSearchCV(svc, svc_param_grid, cv=3, scoring="f1_macro")
