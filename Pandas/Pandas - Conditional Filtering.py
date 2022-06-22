import numpy as np
import pandas as pd

df = pd.read_csv("tips.csv")
print(df.head())
print(df["total_bill"])
boolenSeries = df["total_bill"] > 40
print(df[boolenSeries])
#print(df["total_bill"].sum() / df["tip"].sum())
print(df[df["sex"] == "Female"])
print(df[df["size"] > 3 ])
print(df[df["price_per_person"] > 5])
print(df[df["smoker"] == "Yes"])
print(df[df["time"] == "dinner"])
#print(df[df["total_bill"]> 40] )

# Şartlı karşılaştırmalar
print(df[(df["total_bill"] > 30) & (df["sex"] == "Female")])
print(df[(df["tip"] > 4) & (df["smoker"] == "No")])
print(df[(df["day"] == "Sun") | (df["day"] == "Sat")])
print(print(df[(df["day"] == "Sun") | (df["day"] == "Sat") | (df["day"] == "Fri")]))
print(df[df["sex"].isin(["Female","Male"])])
print(df[df["total_bill"].isin([29.99,19.99,9.99])])
print(df[df["Payer Name"].isin(["Travis Walters","Emirhan Aydın"])])