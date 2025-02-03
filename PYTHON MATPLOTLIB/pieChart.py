import matplotlib.pyplot as plt
b=["C","C++","Java","Python"]
a=[20,60,80,100]
ex=[0.1,0.0,0.0,0.0]
plt.pie(a,labels=b,colors=["green","orange","blue","yellow"],explode=ex,shadow=True,radius=0.8,startangle=180,rotatelabels=360,labeldistance=0.8,autopct="%0.1f%%")
plt.legend()
plt.show()