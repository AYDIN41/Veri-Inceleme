import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10)
y = 2*x
print(x,"\n",y)
plt.plot(x,y)
plt.title("My Title")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0,8)
plt.ylim(0,15)
plt.savefig("MyFirstPlot.png")
plt.show()
