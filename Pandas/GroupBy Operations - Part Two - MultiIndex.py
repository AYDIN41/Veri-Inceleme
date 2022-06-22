import numpy as np
import pandas as pd

df = pd.read_csv("mpg.csv")

yearCyl = df.groupby(["model_year","cylinders"]).mean()

print(yearCyl)
print(yearCyl.xs(key=70,level="model_year")) # xs ile 2 tane sonucu aynı anda göremiyoruz ama
print(yearCyl.xs(key=4,level="cylinders")) # Bir eş özellikleri farklı indexleri bir araya getirebiliyor

#Birden fazla multiIndexleri özelleştirmek istediğimizde groupby methodunu kullanabiliriz
print(df[df["cylinders"].isin([6,8])].groupby(["model_year","cylinders"]).mean())

"""yearCyl = df.groupby(["cylinders","model_year"]).mean()
print(yearCyl)"""
#print(yearCyl.swaplevel())
yearCyl2 = yearCyl.swaplevel()
print(yearCyl.sort_index(level="model_year",ascending=False))
print(yearCyl2.sort_index(level="cylinders",ascending=False))
print(df.agg(["std","mean"]).transpose()) #Birden fazla methodu bir araya toplamayı gösterir
print(df.agg({"mpg":["max","mean"],"weight":["mean","std"]})) #Output da görüldüğü gibi tüm istenilen methodlar index içerisinde gösterilir eşleşmeyen methodlar NaN olarak gözükür



