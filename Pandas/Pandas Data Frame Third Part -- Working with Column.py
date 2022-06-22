import numpy as np
import pandas as pd

df = pd.read_csv("tips.csv")
print(df.describe())
print("\n",df["total_bill"])
mycolumnDataFrame = ["total_bill","tip"]
print(df[mycolumnDataFrame])
#print(df["total_bill","tip"]) Bu şekilde çalışmaz çünkü data frame in içine bir list yazmamız gerekiyor
print(df[["total_bill","tip"]])
#İki veya daha fazla series arasında 4 işlem yapma
print(df["tip"] + df["total_bill"])
print(100 * df["tip"] / df["total_bill"] )
df["Tip_Percentage"] = 100 * df["tip"] / df["total_bill"]
print(df.head())
print(df["price_per_person"])
print(df.info())
df["price_per_person"] = df["total_bill"] / df["size"]
print(df["price_per_person"])
df["price_per_person"] = np.round(df["total_bill"] / df["size"],2)
print(df["price_per_person"])
df["Tip_Percentage"] = np.round(100 * df["tip"] / df["total_bill"],2)
print(df["Tip_Percentage"])

print(df.drop("Tip_Percentage",axis=1).head())
print(df.head())



