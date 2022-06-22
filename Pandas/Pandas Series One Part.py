import numpy as np
import pandas as pd

myData = [1776,1867,1821]
myIndex = ["USA","Canada","Mexico"]
mySer = pd.Series(data=myData)
print(mySer)
#print(type(mySer))
#mySer = pd.Series(data=myData,index=myIndex)
#Kısa yolu veya daha kullanışlı yolu bir alt satırda
mySer = pd.Series(myData,myIndex)
print(mySer)
ages = {"Aydın":21,"Erhan":22,"Kenan":3}
myDicSer = pd.Series(ages)
print(myDicSer)

q1 = {"Japan":80,"China":450,"India":200,"USA":250}
q2 = {"Brazil":100,"China":500,"India":210,"USA":260}

salesQ1 = pd.Series(q1)
salesQ2 = pd.Series(q2)

print(salesQ1)
print(salesQ2)

print(salesQ2.keys())

print(salesQ1 * 3) # Bu işlemi list(diziler) ile yapamayız pandas numpy gibi arraylarını dinamik kullanabiliyor
print(salesQ2 + salesQ1) # İki series de bulunmayan değerler not a number olarak kabul ediliyor
print(salesQ2.add(salesQ1,fill_value=0)) #İki series toplayıp kaçırılan sayıları 0 olarak varsaydık fill_value değerine ne verirsek onu kaçırılan sayı olarak ekleyecek

