import numpy as np
arrayZeros = np.zeros(10)
print(arrayZeros)
arrayOnes = np.ones(10)
print(arrayOnes)
myArr = np.arange(10,51)
print(myArr)
myEvenArr = np.arange(10,51,2)
print(myEvenArr)
myMatrixArr = np.arange(0,9).reshape(3,3)
print(myMatrixArr)
np.random.seed(41)
myRandomNumber = np.random.rand()
print(myRandomNumber)
myRandomMatrix = np.random.randn(25).reshape(5,5)
print(myRandomMatrix)
np.random.seed(42)
myFallowingArr = np.arange(1,101)/100
myFallowingArr.reshape(10,10)
print(myFallowingArr)

myTrialArr = np.random.rand(20).reshape(4,5)
print(myTrialArr)

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])
a = mat[2:,1:]
print(a[1][3])
print(mat)
print(mat[0:3,1:2])
print(mat)
print(mat[4:])
print(mat[3:])
print(mat.sum())
print(mat.std())
print(mat.sum(axis=0))
print(mat.sum(axis=1))
print(myFallowingArr)
arr2 = np.ones(10) * 5
print(arr2)
arr3 = np.eye(3)
print(arr3)