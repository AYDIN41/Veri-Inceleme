import numpy as np
import pandas as pd

df = pd.read_csv("tips.csv")
print(df)
#Her index unique bir yapıya sahiptir bunu column için söyleyemeyiz nasıl column u bir index'e çeviririz şimdi göreceğiz
df = df.set_index("Payment ID")
print(df)
print(df.reset_index()) # Rowları eski haline getirir ve bulunan index'i column'a atar
print(df)
df = df.reset_index()
print(df)
df = df.set_index("Payment ID")
print(df)
print(df.iloc[42]) # int ile istenilen row'u çağırma
print(df.loc["Sat2657"])
print(df.iloc[35:71])
print(df.loc[["Sun2021","Sun1118"]])
print(df.drop("Sun2959"))
print(df.append(["Sun2959"]))
