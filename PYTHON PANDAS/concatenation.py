import pandas as pd
a=pd.DataFrame({
    "name":["Rahul Raj","Rohan Raj","Sakshi Kumari","Pihu Kumari"]
})
b=pd.DataFrame({
    "age":[19,18,16,10]
})
d=pd.DataFrame({
    "name":["Manjusha Sinha","Hemant Kumar Sinha","Alka Sinha","Basant Kumar Sinha"]
})
c=pd.concat([a,b],axis=1)
print(c)

e=pd.concat([a,d],ignore_index=True)
print(e)
