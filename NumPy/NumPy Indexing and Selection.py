import numpy as np
arr = np.arange(0,10)
print(arr[7])
print(arr[0:3])
print(arr[:3])#Bir üsteki ile aynı işlevi yapıyor
print(arr[5:])
print(arr[5:7])

"""myarray = [0,1,2,3,4,5,6,7,8,9]
print(myarray)
myarray[0:5] = 100
print(myarray)""" #Bu işlem kabul görmez çünkü listelere sadece yinelebilir şekilde atama yapılabilir

arr[0:5] = 41
print(arr)

arr = np.arange(0,11)

sliceOfArray = arr[0:5]
print(sliceOfArray)
#Bu şekilde kullanılırsa sliceofArray aldığı arrayleri ve aldığı yerleri değiştirir pointer işlevi görür
sliceOfArray[:] = "77"
print(sliceOfArray)
print(arr)
#Bu şekilde yapıldığında kopyalanan değişken kopya gibi davranır pointer gibi değil
arr = np.arange(0,11)
arrCopy = arr.copy()
arrCopy[:] = 41
print(arrCopy)
print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d.shape)
print(arr2d[0][2])
#Üst tarafta yapılan işlemin aynısı virgül ile aynı kare parentezin içerisinde yazmak daha kullanışlı
print(arr2d[0,2])
print(arr2d[:2,0:2])
print(arr)
print(arr>4)
boolenArray = arr > 4
print(arr[boolenArray])
print(arr[arr>4])