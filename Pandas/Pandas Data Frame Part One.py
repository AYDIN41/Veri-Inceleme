import numpy as np
import pandas as pd
np.random.seed(101)
myRandomArray = np.random.randint(0,101,(4,3))
print(myRandomArray)
myIndex = ["CA","NY","AZ","TX"]
myColumn = ["Jan","Feb","Mar"]

df = pd.DataFrame(myRandomArray,myIndex,myColumn)
print(df.describe())
print(df)
print(df.info())
df2 = pd.read_csv("tips.csv")
print(df2)