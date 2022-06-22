import numpy as np
myArr = np.arange(0,10)
print(myArr)
print(myArr + 5)
print(myArr - 4)
#Numpy arrayleri kendi aralarında 4 işlem yapıyor ama bölmede 0/0 tanımsız sonucu için uyarı veriyor
#Numpy arrayleri 0/0 0/1 bir gibi tanımsız sonuçlar için nan(not a number) alırken int sayılar error alır
print(myArr + myArr)
print(myArr * myArr)
print(myArr / myArr)
print(1 / myArr)
#Bu işlemde de görüldüğü gibi 1/0 işlemi numpy dışında hata verir
#print(1/0)

# Numpy ile aritmetik işlemlerde yapabiliyoruz<
print(np.square(myArr))
print(np.sin(myArr))
print(np.log(myArr))

print(myArr.max())
print(myArr.min())
print(myArr.mean()) #Arrayın ortalmasını alır
print(myArr.var()) #Arrayın varyansını alır
print(myArr.std()) #Arrayın standart sapmasını alır

arr2d = np.arange(0,25).reshape(5,5)
print(arr2d.shape)
print(arr2d)
print(arr2d.sum())
print(arr2d.sum(axis = 0))
print(arr2d.sum(axis=1))

account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])
account_total = account_transactions.sum()
print(account_total)
