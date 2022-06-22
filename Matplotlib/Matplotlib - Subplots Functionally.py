import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,10,11)
b = a ** 4

x = np.arange(0,10)
y = 2 * x

z = np.arange(40,50)
e = z//2

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(9,7),dpi=150)
print(type(axes))
"""axes[0][0].plot(x,y)
axes[0][1].plot(x,e)

axes[1][0].plot(x,e)
axes[1][1].plot(x,z)"""
print(type(axes))


axes[0][0].plot(x,y)
axes[0][1].plot(z,e)

axes[1][0].plot(a,b,"r")
axes[1][0].set_xlabel("X LABEL")
axes[1][0].set_ylabel("Y LABEL")
axes[1][0].set_title("My Special Graph")
axes[1][1].plot(e,y)
axes[1][1].set_ylim(0,14)
"""fig.subplots_adjust(wspace=0.7,hspace=0.7)"""
fig.suptitle("Aydın41")
plt.tight_layout()
#fig.set_figwidth(11)
#fig.savefig("Subplots.png",bbox_inches="tight")
plt.show()