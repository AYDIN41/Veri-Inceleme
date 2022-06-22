import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,11,10)
fig = plt.figure(dpi=100)

ax = fig.add_axes([0,0,1,1])

ax.plot(x,x,label= "X vs X")
ax.plot(x,x**2,label = "X vs X^2")
#ax.legend(loc = (1.1,0.5))
ax.legend(loc = (-0.4,0.5)) #Firstly we write in the tuple as left and bottom line and then we can assign negative number to see number in outside of graph

x = np.linspace(0,11,10)

fig = plt.figure(dpi = 100)

ax = fig.add_axes([0,0,1,1])

#ax.plot(x,x,color= "purple") #We can customize our color what we want to select on the RGB Hex Code we can find hex code by writing in the google

ax.plot(x,x,color= "#468a8a",label="X vs X") # Here it is a hex code

ax.plot(x,x+1,color = "#6fa31a",label = "X vs X+1")

ax.legend(loc = (1.1,0.45))

x = np.linspace(
    0,
    11,
    10)

fig = plt.figure(
    dpi=100)

ax = fig.add_axes(
    [
        0,
        0,
        1,
        1])

# ax.plot(x,x,color= "purple") #We can customize our color what we want to select on the RGB Hex Code we can find hex code by writing in the google

# possible linestyle options '--' '-' '-.' ':'

# ax.plot(x,x,color= "#468a8a",lw=5,linestyle = "--") # LW is adjusted to thick of stick.

# ax.plot(x,x+1,color = "#6fa31a",linewidth=12,ls = "-") #linewidth and lw are same thing

# ax.plot(x,x+2,color = "green",lw=3,ls="-.")
# lines = ax.plot(x,x+3,color = "purple",lw = 1.5,marker = 2,ls = ":")

ax.plot(
    x,
    x + 3,
    color="purple",
    lw=1.5,
    marker=2,
    ls=":",
    ms=15,
    markerfacecolor="black",
    markeredgewidth=5,
    markeredgecolor="grey")

ax.plot(
    x,
    x + 5,
    color="yellow",
    lw=1.5,
    marker="*",
    ls=":",
    markersize=12

    )  # Markersize and ms are same thing

# type(lines[0])
# This is for that customize our graph
# lines[0].set_dashes([2,3,5,3]) #This progress goes like full number of dat and other number example second represents blank

plt.show()
