import pandas as pd
a=pd.read_csv("C:\\Users\\rohan\\Downloads\\DEMO DROPNA.csv")

# DELETE NULL VALUES ROW WISE
#a.dropna(inplace=True) 
#print(a.isnull().sum())

# DELETE NULL VALUES COLUMN WISE

#print(a)
#a.dropna(axis=1,inplace=True)  # CHANGES IN ORIGINAL DATASET SO WE NEED TO PASS INPLACE PARAMETER
#s=a.dropna(axis=1) # CHANGES IN ANOTHER VARIABLE
#print(s)

# DELETE NULL VALUES OF SPECIFIC COLUMN
#a.dropna(subset=["Units"],inplace=True)
#print(a)

a.dropna(thresh=3)
print(a)