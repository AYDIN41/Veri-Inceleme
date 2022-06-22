import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,11,10)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x)

plt.show()