import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[3,5,7,9]
plt.step(a,b,ms=4,mfc="yellow",marker="o",color="green",label="Data Visualization")
plt.legend()
plt.show()