import numpy as np
import pandas as  pd

df = pd.read_csv("tips.csv")

print(df.sort_values("tip",ascending=False))
print(df.sort_values(["tip","size"]))

print(df["total_bill"].max())
print(df["total_bill"].idxmax())
print(df.iloc[170])

print(df.corr())
#Kategori değerler için değer alma
print(df["sex"].value_counts())
print(df.info())
print(df["day"].value_counts())
print(df[["smoker","sex"]].value_counts())
print(df[["day","sex"]].value_counts())

#Unique ve Nunique methodları ile çalışmak data frame içerisindeki tek olan isimleri verir
print(df["day"].unique())
print(df["day"].nunique())

#Replace methodu data frame in içerisinden değiştirmek istediğiniz verileri değiştirir

print(df["sex"].replace("Male","M"))
print(df["sex"].replace(["Male","Female"],["M","F"]))

mymap = {"Female" : "F","Male" : "M"}
print(df["sex"].map(mymap))
print(df.duplicated())

simple_df = pd.DataFrame([1,2,2,3,4],["A","B","C","D","E"])
print(simple_df.duplicated())
print(simple_df.drop_duplicates())
#Aralıklı olarak gösteren data frame uzantısı between'i göreceğiz
print(df[df["total_bill"].between(10,20,inclusive=True)])
#En büyük olan verileri sıralamak için kullanılan methodu göreceğiz
print(df.nlargest(4,"total_bill"))
#print(df.sort_values("total_bill",ascending=False)[0:2])
print(df.nsmallest(3,"tip"))
print(df.sample(9))
print(df.sample(frac=0.05))