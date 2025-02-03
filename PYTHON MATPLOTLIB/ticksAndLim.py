import matplotlib.pyplot as plt
a=[2,4,6,12]
b=[10,20,30,40]
plt.plot(a,b)
plt.xticks(a)
plt.yticks(b)
plt.xlim(2,14)
plt.ylim(10,50)
plt.show()