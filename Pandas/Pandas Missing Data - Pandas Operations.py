import numpy as np
import pandas as pd

df = pd.read_csv("movie_scores.csv")
print(np.nan)
print(np.nan == np.nan)
print(df)

#Data framelerin boş mu yoksa dolu mu olduklarını kontrol için isnull() ve notnull() methodlarını kullanıyoruz
print(df.isnull())
print(df.notnull())
print(df["pre_movie_score"].notnull())
print(df[df["pre_movie_score"].notnull()])
df["sex"]= df["sex"].replace(["m","f"],["Male","Female"])
print(df)

print(df[(df["pre_movie_score"].isnull()) & df["first_name"].notnull()])

#Drop methodu göreceğiz istenmeyen bazı veriler için düşürme işlemi
#Eksik verisi olan tüm satırları düşür anlamına gelir
print(df.dropna())
#Koşul koymak için thresh methodu kullanılabilir buradaki amaç kaç tane nonnull olmayan değeri var bunları görmek
print(df.dropna(thresh=1)) # Görüldüğü gibi Hugh jackman satırı en az 4 tane değişken içerdiği için düşmüyor
print(df.dropna(thresh=5)) # 4 değişken içerdiği için thresh=5 dersek Hugh Jackman satırı düşmüş olur

print(df.dropna(axis=1)) # Column değeri için işlem yapar ama bu tavsiye edilen bir durum değildir column başına bir değere baktığı için thresh kullanmak burada saçma olur

print(df.dropna(subset="first_name")) # Belirtilen column da düşürme işlemi yapar

print(df.fillna("Aydın41"))
print(df["pre_movie_score"].fillna(0)[1])
"""a = 9.0
df["pre_movie_score"][2] = a"""
print(df["pre_movie_score"].fillna(df["pre_movie_score"].mean()))
print(df.fillna(df.mean()))
airlineTicket = {"first":100,"business":np.nan,"economy-plus":50,"economy":30}
ser = pd.Series(airlineTicket)
print(ser)
print(ser.interpolate())