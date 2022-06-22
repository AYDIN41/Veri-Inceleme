import numpy as np
import matplotlib.pyplot as plt

"""m = np.linspace(0,10,11)
print(f"The array of m should look like this :\n\n{m}")

c = 3 * 10 ** 8 # Işık hızı

E = m*c**2

print(f"The array of E should look like this :\n\n{E}")

plt.plot(m,E,color = "red",lw = 5)
plt.title("E=mc^2")
plt.ylabel("Energy in Joules")
plt.xlabel("Mass in Grams")
plt.yscale("log")
plt.ylim(10**0,10**18)
plt.show()"""

labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

f"""ig = plt.figure()
ax = fig.add_axes([0,0,1,1])"""
"""ax.plot(labels,july16_2007,label = "july16_2007,label")
ax.plot(labels,july16_2020,label = "july16_2020,label")
ax.legend(loc = 0)"""

fig,axes = plt.subplots(nrows=2,ncols=1)

axes[0].plot(labels,july16_2007)
axes[1].plot(labels,july16_2020)


labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(labels,july16_2007,label = "july16_2007,label")
ax.plot(labels,july16_2020,label = "july16_2020,label")


fig,axes = plt.subplots(nrows=2,ncols = 1,figsize=(12,8))

axes[0].plot(labels,july16_2020)
axes[1].plot(labels,july16_2007)
axes[0].set_title("July 16th, 2007")
axes[1].set_title("July 16th 2020")
ax.legend(loc = 0)

labels = [
    '1 Mo',
    '3 Mo',
    '6 Mo',
    '1 Yr',
    '2 Yr',
    '3 Yr',
    '5 Yr',
    '7 Yr',
    '10 Yr',
    '20 Yr',
    '30 Yr']

july16_2007 = [
    4.75,
    4.98,
    5.08,
    5.01,
    4.89,
    4.89,
    4.95,
    4.99,
    5.05,
    5.21,
    5.14]
july16_2020 = [
    0.12,
    0.11,
    0.13,
    0.14,
    0.16,
    0.17,
    0.28,
    0.46,
    0.62,
    1.09,
    1.31]

fig = plt.figure(
    figsize=(
    10,
    7))

a1 = fig.add_axes(
    [
        0,
        0,
        1,
        1])
a1.plot(
    labels,
    july16_2007,
    color="blue")
a1.set_ylabel(
    "2007",
    color="blue")
a1.spines[
    "left"].set_color(
    "blue")
a1.spines[
    "left"].set_linewidth(
    4)
for label in a1.get_yticklabels():
    label.set_color(
        "blue")

a2 = a1.twinx()
a2.plot(
    labels,
    july16_2020,
    color="red")
a2.set_ylabel(
    "2020",
    color="red")
a2.spines[
    "right"].set_color(
    "red")
a2.spines[
    "right"].set_linewidth(
    4)
for label in a2.get_yticklabels():
    label.set_color(
        "red")

a1.set_title(
    "July 16th Yield Curves")
plt.tight_layout()


plt.show()