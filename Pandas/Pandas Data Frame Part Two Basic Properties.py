import numpy as np
import pandas as pd

df2 = pd.read_csv("tips.csv")
print(df2)
print(df2.columns)
print(df2.index)
print(df2.head()) #Belirlenen data ve .head yukarıdan aşağıya istenilen kadar içerik verir
print(df2.head(42))
print(df2.tail()) #.tail ise belirlenen verilerin asğıdan yukarıya verir
print(df2.info())
print(df2.describe())
print(df2.describe().transpose())