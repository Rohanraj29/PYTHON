import pandas as pd
a=pd.DataFrame({
    "a":[2,4,6,8],
    "b":[10,12,14,16]
})
a.insert(0,"Rahul",[18,20,22,24])
print(a)