import pandas as pd
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\CHANGE DATATYPE.csv")
a.pop("column_5")
print(a.dtypes)
a["Amount"]=a["Amount"].astype(float)
a["Age"]=a["Age"].astype("Int32")
a["Name"]=a["Name"].astype("string")
print(a)
print(a.dtypes)