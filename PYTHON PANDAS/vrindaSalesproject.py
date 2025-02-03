import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\Vrinda-Store-Data-Analysis.csv")
print(a)
specified=a.loc[a['ship-state']=="Bihar"]
b=specified['Gender']
c=specified['Amount']
plt.bar(b,c)
plt.show()