# WHEN WE WANT TO CHANGE THE SHAPE OF AN ARRAY THEN WE CAN USE RESHPING FUNCTION.
import numpy as np

# CONVERTING 1D ARRAY INTO A 2D ARRAY

a=np.array([2,4,6,8])
b=a.reshape(2,2)
print(a)
print(a.shape)
print(b)
print(b.shape)

# CONVERTING 1D ARRAY INTO A 3D ARRAY
c=a.reshape(1,2,2)
print(c)
print(c.shape)

# CONVERTING 2D ARRAY INTO A 3D ARRAY
d=np.array([[2,4,6,8],[10,12,14,16]])
e=d.reshape(2,2,2)
print(d)
print(d.shape)
print(e)
print(e.shape)

# CONVERTING 2D ARRAY INTO A 1D ARRAY
f=d.reshape(-1)
print(f)
print(f.shape)

# CONVERTING 3D ARRAY INTO A 2D ARRAY
g=np.array([[[2,4,6,8],[10,12,14,16]],[[18,20,22,24],[26,28,30,32]]])
h=g.reshape(4,4)
print(g)
print(g.shape)
print(h)
print(h.shape)

# CONVERTING 3D ARRAY INTO A 1D ARRAY
i=g.reshape(-1)
print(i)
print(i.shape)