import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,10,11)
b = a ** 4
print(a)
print(b)

x = np.arange(0,10)
print(x)
y = 2*x
print(y)

fig = plt.figure()

axes1 = fig.add_axes([0,0,1,1]) #Jupiter notebook'a tam olarak gözükecektir
axes = fig.add_axes([1,1,0.4,0.4])
axes1.plot(a,b)


axes.plot(a,b)
axes.set_xlim(1,3)
axes.set_ylim(0,250)
axes.set_xlabel("A")
axes.set_ylabel("B")
axes.set_title("Zoomed In")
plt.show()
