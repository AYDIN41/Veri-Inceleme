import numpy as np
import pandas as pd
from datetime import datetime

myYear = 2000
myMonth = 6
myDay = 18
myHour = 2
myMin = 17
mySec = 41
myDate = datetime(myYear,myMonth,myDay) # Alınan değişkenleri datetime methodunun içerisine atıyoruz
print(myDate)
myDate2 = datetime(myYear,myMonth,myDay,myHour,myMin,mySec)
print(myDate2)
print(myDate2.year," ",myDate2.minute)

#Pandas ile datetime kullanımı
myser = pd.Series(["Nov 3 1990","2000-01-01",None])

print(myser) #Burada görüldüğü gibi veri tipi object'tir ve buradan year minutes gibi özellikleri alamıyoruz çünkü değişkenler string gibi hareket ediyor
#print(myser[0].year)
myser2 = pd.to_datetime(myser)
print(myser2) #Görüldüğü gibi burada da dateTime özelliği sergiliyor
print(myser2[0].year)
euroDate  = "31-12-2000"
trialDate = pd.to_datetime(euroDate,infer_datetime_format=True)
print(trialDate)
euroDate = "10-12-2000"
realEuroDate = pd.to_datetime(euroDate,dayfirst=True)
print(realEuroDate)
#Pandas pd_DateTime için özelleştirilmiş format uygulamasını görüyoruz
styleDate = "12--Dec--2000"
realStyleDate = pd.to_datetime(styleDate,format="%d--%b--%Y")
print(realStyleDate)
#Pandas özelleştirilmiş averi anlama özelliğini göreceğiz
custom = "12th of December 2000"
customDate = pd.to_datetime(custom)
print(customDate)

dateDf = pd.read_csv("RetailSales_BeerWineLiquor.csv")
print(dateDf)
print(dateDf["DATE"])
dateDf["DATE"] = pd.to_datetime(dateDf["DATE"]) # Burada string olan data tipini datetime'a çeviriyoruz
print(dateDf["DATE"])
#parse_date yöntemi kolaylıkla bir column'u datetime tipine çevirebiliriz
sales = pd.read_csv("RetailSales_BeerWineLiquor.csv",parse_dates=[0])
print(type(sales))
#Time methodları ile groupby yöntemi benzeri bir yeniden örnek oluşturma
"""sales = sales.set_index("DATE")
print(sales)
print(sales.resample(rule="AS").mean())
print(sales.resample(rule="AS").mean()) #39.dersin 18.57 dk'sında rule dağılımları gösteriliyor
print(sales.resample(rule="M").mean())"""
print(sales["DATE"].dt.month)
print(sales["DATE"].dt.year)
print(sales["DATE"].dt.day)
