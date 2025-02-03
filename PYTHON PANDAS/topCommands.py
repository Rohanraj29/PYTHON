import pandas as pd
a=pd.DataFrame({
    "name":["Rahul","Rohan","Sakshi","Pihu"],
    "age":[19,18,16,10]
})

# CREATING NEW COLUMN IN PANDAS

a["city"]=["Muzaffarpur","Aghoriya Bazar","Neem Chowk","Muzaffarpur"]

# RENAMING A COLUMN NAME

a.columns=["Name","Age","City"]

# DELETING A COLUMN IN PANDAS
a.drop(["Age"],axis=1)

a.sort_index(ascending=True)
print(a)