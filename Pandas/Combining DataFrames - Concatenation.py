import numpy as np
import pandas as pd

dataOne = {"A": ["A0","A1","A2","A3"],"B":["B0","B1","B2","B3"]}
dataTwo = {"C" : ["C0","C1","C2","C3"],"D": ["D0","D1","D2","D3"]}

one = pd.DataFrame(dataOne)
print(one)
two = pd.DataFrame(dataTwo)
print(two)
#İki dizini birleştirme işlemi
print(pd.concat([one,two],axis=1))
print(pd.concat([one,two],axis=0))
#İki column ismi farklı data frame'i birleştirirken iki ayrı data framelerin column isimlerini aynı yaparsak NaN almaktan kurtuluruz
two.columns = one.columns
print(pd.concat([one,two],axis=0))
myDf = pd.concat([one,two],axis=0)
print(myDf.index)
myDf.index = np.arange(1,9)
# myDf.index = range(len(myDf))
print(myDf.index)
print(myDf)
