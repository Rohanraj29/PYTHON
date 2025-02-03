import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\Vrinda-Store-Data-Analysis.csv")
a.pop("B2B")
print(a)
print(a.isnull().sum())
a.replace(to_replace="W",value="Women",inplace=True)
a.replace(to_replace="M",value="Men",inplace=True)
print(a)
print(a.iloc[10,3])
b=a["Gender"]
c=a["Amount"]
d=a["ship-state"]
#plt.bar(b,c)
plt.plot(d,b)
plt.show()