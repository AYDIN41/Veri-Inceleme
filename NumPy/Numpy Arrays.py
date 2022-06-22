import \
    random

import numpy as np
mylist = [1,2,3,4]
print(list(mylist))
print(np.array(mylist))
print(type(mylist))
myarr = np.array(mylist)
print(myarr)
print(type(myarr))

myMatrix = [[1,2,3],[4,5,6],[7,8,9]]
print(myMatrix)
print(np.array(myMatrix))

#np.arange range fonksiyonuna eş olan bir method
print(np.arange(35,42,2))
print(np.zeros(5))
print(np.zeros((5,5)))
print(np.zeros((2,),dtype=[('x',float),('y',int)]))

#Linspace belirli aralıklarla range işlemi uygular
print(np.linspace(0,10,101))
print(len(np.linspace(0,10,41)))

#Eye fonksiyonu
print(np.eye(4))

#Random fonksiyonu ile çalışmak
print(np.random.rand(2,4))

#Randn fonksiyonu ile normal standart sapma ile ilgili örnekler verilebilir alınan örneklerin değerini z tablosundan öğrenebiliriz
print(np.random.randn(2,3))
print(np.random.randint(0,101,3))
print(np.random.randint(0,101,(3,4)))

#Seed fonksiyonu belirli bir sample oluşturur ve kullanılan seed örnekleri her yerde aynıdır
np.random.seed(41)
print(np.random.rand(4))

#Reshape fonksiyony
arr = np.arange(0,25)
print(arr)
print(arr.reshape(25,1))
#Min max ve argmax argmin
mynpList = np.random.randint(0,101,11)
print(mynpList)
print(mynpList.max())
print(mynpList.min())
print(mynpList.mean()) #Ortalamasını alır
print(mynpList.sum()) # Array de ki sayıların toplamını alır
print(mynpList.argmax())#Array içerisindeki en büyük sayının olduğu index'i gösterir
print(mynpList.argmin())#Array içerisindeki en küçük sayının olduğu index'i gösterir
outarray = mynpList.argsort()#Arrayları küçükten büyüğe sıralar
print(mynpList[outarray])
print(mynpList.dtype)#Ne kadar yer kapladığını gösteriyor
print(mynpList.shape) # Şeklinin nasıl olduğunu gösteriyor









