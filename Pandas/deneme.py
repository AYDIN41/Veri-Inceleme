import pandas as pd
import numpy as np
import os
#Csv dosyaları okuma dersi için

print(os.getcwd())
df = pd.read_csv("example.csv",index_col=0)
print(df)
df.to_csv("C:\\Users\\asus\\Desktop\\newfile.csv")