import pandas as pd
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\DEMO DROPNA.csv")

# FILLING SAME VALUE IN ALL THE COLUMN THAT CONTAINS A NULL VALUE
a.fillna(220,inplace=True)
print(a)

# FILLING VALUE IN A SPECIFIC COLUMN
a["Units"].fillna(480,inplace=True)
print(a)

#FILLINGS DIFFERENT VALUE IN DIFFERENT COLUMNS

a.fillna({"Units":480,"Unit_price":440,"Sale_amt":500},inplace=True)
print(a)


# FILLING NULL VALUES USING MEAN
m=a["Units"].mean()
a["Units"].fillna(m,inplace=True)
print(a)

# FILLING NULL VALUES USING MEDIAN
m=a["Units"].median()
a["Sale_amt"].fillna(m,inplace=True)
print(a)

# FILLING NULL VALUES USING MODE
m=a["Units"].mode()[0]
a["Units"].fillna(m,inplace=True)
print(a)

a.pop("Units")
print(a)