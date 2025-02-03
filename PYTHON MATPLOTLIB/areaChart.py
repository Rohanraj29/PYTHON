import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[3,5,7,9]
c=[4,8,12,16]
d=[20,24,28,21]
plt.stackplot(a,b,c,d,labels=["data1","data2","data3"],colors=["yellow","green","blue"])
plt.legend()
plt.show()