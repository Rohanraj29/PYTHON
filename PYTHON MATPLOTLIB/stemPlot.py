import matplotlib.pyplot as plt
a=[2,4,6,8]
b=[3,5,7,9]
plt.stem(a,b,linefmt=":",basefmt="yellow",markerfmt="green",bottom=8,orientation="horizontal",label="Data visualization")
plt.legend()
plt.show()