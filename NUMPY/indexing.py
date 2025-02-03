# BY USING INDEXING WE CAN ACCESS ELEMENT OF ANY POSITION

import numpy as np
# INDEXING IN 1D ARRAY

a=np.array([2,4,6,8])
print(a[0])
print(a[2])

# INDEXING IN 2D ARRAY
b=np.array([[2,4,6,8],[10,12,14,16]])
print(b[0,2]) # ACCESSING ELEMENT AT 0 ROW/INDEX AND 2ND INDEX/COLUMN
print(b[1,2]) # ACCESSING ELEMENT AT 1 ROW/INDEX AND 2ND INDEX/COLUMN

# INDEXING IN 3D ARRAY
c=np.array([[[2,4,6,8],[10,12,14,16]],[[18,20,22,24],[26,28,30,32]]])
print(c[0,0,3])
print(c[0,1,3])
print(c[1,0,1])
print(c[1,1,2])