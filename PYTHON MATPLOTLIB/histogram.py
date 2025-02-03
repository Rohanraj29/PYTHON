import matplotlib.pyplot as plt
import numpy as np
import random
mi=np.random.randint(10,40,(8))
csk=np.random.randint(50,80,(8))
b=[10,20,40,60,80,100]
plt.hist([mi,csk],bins=b,range=(0,90),color=["green","orange"],rwidth=10,cumulative=-1,orientation="horizontal",label=["Mumbai Indians","Chennai super kings"],bottom=28)
plt.legend()
plt.show()