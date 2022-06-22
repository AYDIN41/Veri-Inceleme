import numpy as np
import pandas as pd

email = "eydin4111@gmail.com"
print(email.split("@"))

names = pd.Series(["andrew","bobo","claire","david","5"])
print(names)
print(names.str.upper())
print(names.str.isdigit())
print(names[names.str.isdigit()])
techFinance = ["GOOG,APPL,AMZN","JPM,BAC,GS"]
print(len(techFinance))
tickers = pd.Series(techFinance)
print(tickers)
print(tickers.str.split(","))
tech = "GOOG,APPL,AMZN"
print(tech.split()[0])
print(tickers.str.split(",").str[0])
print(tickers.str.split(",").str[0][0])
print(tickers.str.split(",",expand=True))

messyNames = pd.Series(["andrew     ","bo:bo","     claire      "])
print(messyNames)
print(messyNames[0])
print(messyNames.str.replace(":",""))
print(messyNames.str.replace(":","").str.strip())
print(messyNames.str.replace(":","").str.strip().str.capitalize())

def cleanName(name):
    name = name.replace(":","")
    name = name.strip()
    name = name.capitalize()
    return name
print(messyNames.apply(cleanName))