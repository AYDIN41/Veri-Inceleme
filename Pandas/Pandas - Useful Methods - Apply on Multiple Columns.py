import numpy as np
import pandas as pd

df = pd.read_csv("tips.csv")

print(df.head())
def quality(price,tip):
    if tip/price > 0.15:
        return "Perfect Tip"
    else:
        return "Mediocre Tip"
df["Tip Measure"] = df[["total_bill","tip"]].apply(lambda a: quality(a["total_bill"],a["tip"]),axis=1 )
print(df.head())

def meanOfMoney(totalBill,tip,size):
    return (totalBill + tip) / size
print(df.info())
df["Mean of Money"] = df[["total_bill","tip","size"]].apply(lambda df: meanOfMoney(df["total_bill"],df["tip"],df["size"]),axis=1)
print(df.head())

def generousWomen(tipMeasure,sex):
    if tipMeasure == "Perfect Tip" and sex == "Female":
        return "Generous Women"
    elif tipMeasure == "Perfect Tip" and sex == "Male":
        return "Generous Men"
    else:
        return "Customer"
df["Woman Tip Measure"] = df[["Tip Measure","sex"]].apply(lambda df:generousWomen(df["Tip Measure"],df["sex"]),axis=1)
print(df.head())

def smokerGender(smoker,sex):
    if smoker =="Yes" and sex == "Male":
        return "Smoker Man"
    elif smoker == "Yes" and sex == "Female":
        return "Smoker Woman"
    else:
        return "Healthy Person"
df["Smoker Measure"] = df[["smoker","sex"]].apply(lambda df:smokerGender(df["smoker"],df["sex"]),axis=1)
print(df.head())

#Vectorize methodunu kullanma
df["Quality"] = np.vectorize(quality)(df["total_bill"],df["tip"])
print(df.head())
df["Woman Tip Measures"] = np.vectorize(generousWomen)(df["Tip Measure"],df["sex"])
print(df.head())
df["Do not Smoke"] = np.vectorize(smokerGender)(df["smoker"],df["sex"])
print(df.head())
df["meanOfNothing"] = np.vectorize(meanOfMoney)(df["total_bill"],df["tip"],df["size"])
print(df.head())
