import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,11,10)
fig = plt.figure(dpi=100)

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x,label= "X vs X")
ax.plot(x,x**2,label = "X vs X^2")
#ax.legend(loc = "lower left") #loc = "place to locate" yaparsak legend değerini istediğimiz yere göndeririz
#ax.legend(loc = 0) # This loc code will find best locate for the legend
ax.legend(loc = (1.1,0.5)) # We have made legend out of graph but this can not display in pycharm we can see in jupter notebook
plt.show()
