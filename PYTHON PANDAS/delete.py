import pandas as pd
a=pd.DataFrame={
    "name":["Rahul","Rohan","Sakshi","Pihu"],
    "age":[19,18,16,15],
    "city":["Muzz","Sitm","Muzz","Sitm"]
}
a.pop("city")
del a["age"]
print(a)