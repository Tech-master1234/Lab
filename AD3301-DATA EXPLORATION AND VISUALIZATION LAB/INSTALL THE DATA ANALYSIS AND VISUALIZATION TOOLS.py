import pandas as pd
s1 = pd.Series([1, 2])
s2 = pd.Series(["Ashish", "Sid"])
df = pd.DataFrame([s1, s2])
print(df)

dframe = pd.DataFrame([[1, 2], ["Ashish", "Sid"]],
                      index=["r1", "r2"],
                      columns=["c1", "c2"])
print(dframe)

dframe = pd.DataFrame({
    "c1": [1, 2],
    "c2": ["Ashish", "Sid"]
})
print(dframe)

df = pd.read_csv("C:/Users/manoj/OneDrive/Documents/DEV LAB/IND_data.csv")
print("\n",df.head())
print("\n",df.shape)
print(df.iloc[0:5,:]) 
print("\n",df.iloc[:,:])
print("\n",df.iloc[5:,:5])


print("\nFirst five rows including 5th index and all columns:")
print(df.loc[0:5, :])
df = df.loc[5:, :]
print("\nData from the 5th row onwards and all columns:")
print(df)
print("\nFirst 5 rows of the 'Time period' column:")
print(df.loc[:5, "Time period"])

numeric_columns = df.select_dtypes(include='number')
correlation_matrix = numeric_columns.corr()
print(correlation_matrix)
