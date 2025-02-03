import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[3,5,7,9]
plt.subplot(2,2,1)
plt.plot(a,b)
c=[4,8,12,16]
d=[20,22,24,26]
plt.subplot(2,2,2)
plt.plot(c,d)
e=[4,8,12,16]
f=["C","C++","Java","Python"]
plt.subplot(2,2,3)
plt.bar(e,f)
g=[18,20,30,40]
h=["m","h","a","b"]
plt.subplot(2,2,4)
plt.bar(g,h)
plt.show()