import pandas as pd
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\Cars_data.csv")
print(a)
print(a.head(2))
print(a.tail(2))
print(a.info())
print(a.describe())
print(a.isnull().sum())
print(a.index)
print(a.dtypes)
print(a.shape)
print(a.size)
print(a.sample)
print(a.columns)