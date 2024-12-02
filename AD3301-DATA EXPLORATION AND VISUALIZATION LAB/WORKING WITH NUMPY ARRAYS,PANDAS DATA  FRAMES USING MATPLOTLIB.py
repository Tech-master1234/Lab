# Step 1: Import the NumPy module
import numpy as np

# Step 2: Create an ndarray by passing a list, tuple, or any array-like object into the array() method
my_list = [1, 2, 3, 4]
sample_array = np.array(my_list)

# Step 3: Print the list and the NumPy array
print("List in Python:", my_list)
print("NumPy Array in Python:", sample_array)

# Python program to demonstrate creating a DataFrame from a dictionary

# Step 1: Import the Pandas module
import pandas as pd

# Step 2: Initialize data of lists
data = {'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
        'Age': [20, 21, 19, 18]}

# Step 3: Create a DataFrame
df = pd.DataFrame(data)

# Step 4: Print the DataFrame
print(df)
