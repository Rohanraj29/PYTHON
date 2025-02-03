import numpy as np
# SLICING IN 1D ARRAY

a=np.array([2,4,6,8])
print(a[0:2])

# SLICING IN 2D ARRAY

b=np.array([[2,4,6,8],[10,12,14,16]])
print(b[0,0:4])  # SINGLE ROW MULTIPLE COLUMNS
print(b[0:2,1])  # MULTIPLE ROW SINGLE COLUMNS
print(b[0:2,0:4]) # MULTIPLE ROW MULTIPLE COLUMNS