import numpy as np
import pandas as pd
df = pd.read_csv("tips.csv")
print(df.head())

def lastFourLetters(num):
    return int(str(num)[-4:])
#print(lastFourLetters(145341178941))
#print(df["CC Number"].apply(lastFourLetters)) #Burada fonksiyon çağırma işlemi yapmıyoruz sadece fonksiyonun ismini belirtiyoruz apply methhoduy bizim yerimize bunu yapıyor
df["Last Four Digit"] = df["CC Number"].apply(lastFourLetters)
print(df.head())

print(df["total_bill"].mean())
def yelp(money):

    if money > 20:
        return "$$$"
    elif money < 20 and money >14:
        return "$$"
    else:
        return "$"

df["Dolar Sign"] = df["total_bill"].apply(yelp)
print(df.head())

"""def tipPercentage(price,tip):
    return price * (tip/100)
df["TipPercentage"] = df["total_bill","tip"].apply(tipPercentage)
print(df.head())"""