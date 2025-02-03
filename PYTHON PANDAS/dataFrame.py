import pandas as pd

# DATA FRAME OF AN ARRAY
a=pd.DataFrame([[2,4,6,8],[10,12,14,16]])
print(a)
print(a.iloc[0,2])

# DATA FRAME OF A STRING
b=pd.DataFrame({
    "name":["Rahul","Rohan","Sakshi","Pihu"],
    "age":[19,18,16,10]
})
b.to_csv("samplee.csv",index=False)
print(b)
print(b['name']) # ACCESS ELEMENTS USING COLUMN WISE

# ACCESS ELEMENTS USING ROW WISE

print(b.loc[0,"name"]) # in this we have to specify index number and column name which you want to access
print(b.iloc[2,0])   # in this we have to specify index number and column number which you want to access