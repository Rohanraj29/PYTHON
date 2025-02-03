import matplotlib.pyplot as plt
a=["C","C++","Java","Python"]
b=[10,22,30,40]
plt.title("Data Visualization",fontsize=18)
plt.xlabel("Courses",fontsize=18)
plt.ylabel("Interested students",fontsize=18)
plt.bar(a,b,width=0.4,color="green",alpha=0.5,edgecolor="yellow",linewidth=14,align="center",label="Programming language")
plt.legend()
plt.show()