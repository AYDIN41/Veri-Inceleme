import pandas as pd

df = pd.read_csv("Ecommerce Purchases")
print(df)
print(df.head())
print(df.info())
print(df["Purchase Price"].mean())
print(df["Purchase Price"].max())
print(df["Purchase Price"].min())
print(df[df["Language"] == "en"].info())
print(df[df["Job"]=="Lawyer"].info())
print(df["AM or PM"].value_counts())
print(df["Job"].value_counts().iloc[:5])

print(df[df["Lot"] == "90 WT"]["Purchase Price"])
print(df[df["Credit Card"] == 4926535242672853]["Email"])
print(df[(df["CC Provider"] == "American Express") & (df["Purchase Price"] > 95)].count())

print(sum(df["CC Exp Date"].apply(lambda x : x[3:]) == "25"))
print((df["Email"].apply(lambda x: x.split("@")[1]).value_counts().head(5)))