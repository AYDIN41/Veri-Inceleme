import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_html("https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri/Tuketici+Fiyatlari")

print(df[0])
print(df[0].info())
print(df[0]["Unnamed: 0"])

a = df[0]["Unnamed: 0"]

b = df[0]["TÜFE (Yıllık % Değişim)"]

c = df[0]["TÜFE (Aylık % Değişim)"]
a = a.iloc[0:64]
b = b.iloc[0:64]
c = c.iloc[0:64]

a = a.reindex(index=b.index[::-1])
b = b.reindex(index=b.index[::-1])
c = c.reindex(index=c.index[::-1])
print(b)

fig = plt.figure(figsize=(20,10))

ax = fig.add_axes([0,0,1,1])

ax.plot(a,c,color = "purple",label = "Aylık % Değişim",lw=4,ls = ":")
ax.plot(a,b,color = "red",label = "Yıllık % Değişim",lw=4,ls = "--")

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(9,7),dpi=150)

axes[0].plot(a,c,color = "purple",label = "Aylık % Değişim",lw=4,ls = ":")
axes[0].set_xlabel("Yıl")
axes[0].set_ylabel("Aylık % Değişim")

axes[1].plot(a,b,color = "red",label = "Yıllık % Değişim",lw=4,ls = "--")
axes[1].set_xlabel("Yıl")
axes[1].set_ylabel("Yıllık % Değişim")
axes[0].legend()

fig = plt.figure(dpi=100)

fig,ax1 = plt.subplots()

ax1.plot(b,a,lw=2,color="blue")
ax1.set_ylabel(r"Yıllık % Değişim",fontsize=18,color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(c,a,lw=2,color="red")
ax2.set_ylabel(r"Aylık % Değişim",fontsize=18,color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")
plt.yticks(fontsize=15)

fig2 = plt.figure(figsize=(20,10))
ax3 = fig2.add_axes([0,0,1,1])
ax3.scatter(a, c)
ax3.set_title("Enflasyon")
ax3.set_xlabel("Aylık % Değişim")

fig3 = plt.figure(figsize=(20,10))
ax4 = fig3.add_axes([0,0,1,1])
ax4.scatter(a, b)
ax4.set_title("Enflasyon")
ax4.set_xlabel("Yıllık % Değişim")



plt.savefig('test.png', bbox_inches='tight')
ax.legend(loc = 0,prop= {"size" :15})

plt.show()
