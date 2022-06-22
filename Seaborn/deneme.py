import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_html("https://tr.wikipedia.org/wiki/Kocaeli")

print(df[2])

a = df[2][0].drop([0,1,14])
print(a)

b = df[2][1].drop([0,1,14])
print(b)
c = df[2][2].drop([0,1,14])
g = df[2][3].drop([0,1,14])
myList = a + b + c

print(myList)
myList = [
["Başiskele",108.185,111.641],
["Çayırova",140.274,144.825],
["Darıca",214.796,219.546],
["Derince",143.884,144.287],
["Dilovası",51.060,51.866],
["Gebze",392.945,399.558],
["Gölcük",170.503,172.802],
["İzmit",365.893,371.002],
["Kandıra",52.268,52.930],
["Karamürsel",58.412,58.936],
["Kartepe",125.974,131.416],
["Körfez",173.064,174.632]]

df_izmit = pd.DataFrame(myList,columns={"İlçe","Nüfus 2020","Nüfus 2021"})
print(df_izmit.columns)
df_izmit.columns = ["İlçe","Nüfus 2020","Nüfus 2021"]
print(df_izmit)

fig = plt.figure(figsize=(10,5))
fig2 = plt.figure(figsize=(7,5))
ax = fig.add_axes([0,0,1,1])
ax2 = fig2.add_axes([0,0,1,1])
d = df_izmit["Nüfus 2020"]
e = df_izmit["İlçe"]
f = df_izmit["Nüfus 2021"]
newNumber = np.arange(0,12)

print(e)
g.reindex(newNumber)
ax.plot(e,d,lw=4,label="Nüfus 2020")
ax.plot(e,f,lw=4,label="Nüfus 2021")

print(g)
newArray = []
for i in g:
    newArray.append(i)

print(g.reindex_like(df_izmit))
g = g.reindex_like(df_izmit)
for z in range(0,11):
    g[z] = newArray[z]

g.str.strip()
g = g.sort_values()
print(g.info())
ax2.plot(e,g,lw=5,label="2020 - 2021 Nüfus Değişim Sayıları")
ax.legend(loc= 0)
ax2.legend(loc = 0)
plt.show()