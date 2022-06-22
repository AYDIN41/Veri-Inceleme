import \
    numpy as np
import pandas as pd
url = "https://tr.wikipedia.org/wiki/Kocaeli%27nin_il%C3%A7eleri"
df = pd.read_html(url)
print(df)
print(df[4])
df[4] = df[4].dropna(axis=0,thresh=3)
print(df[4].info())
print(df[4]["İlçe"])
print(df[4]["İlçe"][0])
print(df[4].set_index("İlçe"))
#İzmit nüfus verileri
izmitPop = df[4].set_index("İlçe")
print(izmitPop.loc["İzmita"])
pop1 = izmitPop.loc["İzmita"]
pop1.column = "Population"
print(len(pop1))
a = 0
i= 0
"""for pop1 in (0,21) :
    a += pop1[i]
    i += 1"""
#print(a)

while i<21:
    pop1[i] = float(pop1[i])
    a += pop1[i]
    i+= 1
#1975'ten beri izmitin ortalama nüfus verileri
print(round(a/21,3))
print(round(a,3))

#Kocaeli ilçeleri nüfus farkları

avPop = df[3]
print(avPop[0])
#avPop = avPop.set_index(avPop[0])
print(avPop.info())
print("2020 nüfusları\n",avPop[1][2:14])
print("2021 nüfusları\n",avPop[2][2:14])
avPop2020 = list(avPop[1][2:14])
avPop2021 = list(avPop[2][2:14])
print(avPop2020)
avPop2020 = np.array(avPop2020)
avPop2020 = avPop2020.reshape(12,1)
avPop2021 = np.array(avPop2021)
avPop2021 = avPop2021.reshape(12,1)
a = avPop2021[0]


mayor = df[1]
print(mayor[1][2:14])
mayor = mayor[1][2:14]
mayor.index = np.arange(1,13)
print(mayor)
mayor[1] = "Tahir Büyükakın"
mayor[2] = "Mehmet Yasin Özlü"
mayor[3] = "Bünyamin Çiftçi"
mayor[4] = "Muzaffer Bıyık"
mayor[5] = "Zeki Aygün"
mayor[6] = "Hamza Şayir"
mayor[7] = "Zinnur Büyükgöz"
mayor[8] = "Ali Yıldırım Sezer"
mayor[9] = "Fatma Kaplan Hürriyet"
mayor[10] = "Adnan Turan"
mayor[11] = "İsmail Yıldırım"
mayor[12] = "Muhammet Mustafa Kocaman"
print(mayor)

print(df)
print(df[4])
print(df[4].drop(12))
df[4] = df[4].drop(12)
print(df[4])

print(df[4].iloc[0].iloc[0])
df[4].iloc[0].iloc[0] = "İzmit"
print(df[4])
df[4].index = np.arange(1,14)
print(df[4])
df[4].to_html("C:\\Users\\asus\\Desktop\\sample2.html")
df[4][2021] = "A"
print(df[4].columns)
print(df[4])
