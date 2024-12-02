import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
file_path = "C:/Users/manoj/OneDrive/Documents/DEV LAB/iris.csv"
iris = pd.read_csv(file_path, header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

#Understanding Data
print(iris.shape)  # prints no. of rows and columns
print(iris.columns)  # prints name of columns
print(iris["species"].value_counts())

#1D Scatter plot
iris_setosa = iris.loc[iris["species"] == "Iris-setosa"]
iris_virginica = iris.loc[iris["species"] == "Iris-virginica"]
iris_versicolor = iris.loc[iris["species"] == "Iris-versicolor"]

plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_setosa["petal_length"]), 'o', label='Iris-setosa')
plt.plot(iris_versicolor["petal_length"], np.zeros_like(iris_versicolor["petal_length"]), 'o', label='Iris-versicolor')
plt.plot(iris_virginica["petal_length"], np.zeros_like(iris_virginica["petal_length"]), 'o', label='Iris-virginica')
plt.title('1D Scatter Plot of Petal Length')
plt.legend()
plt.grid()
plt.show()

# 2D scatter plot
plt.figure()
plt.scatter(iris.loc[iris["species"] == "Iris-setosa", "sepal_length"], iris.loc[iris["species"] == "Iris-setosa", "sepal_width"], label="Iris-setosa")
plt.scatter(iris.loc[iris["species"] == "Iris-versicolor", "sepal_length"], iris.loc[iris["species"] == "Iris-versicolor", "sepal_width"], label="Iris-versicolor")
plt.scatter(iris.loc[iris["species"] == "Iris-virginica", "sepal_length"], iris.loc[iris["species"] == "Iris-virginica", "sepal_width"], label="Iris-virginica")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("2D Scatter Plot of Sepal Length vs Sepal Width")
plt.legend()
plt.grid()
plt.show()
