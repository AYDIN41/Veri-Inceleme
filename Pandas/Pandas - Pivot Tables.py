import pandas as pd
import numpy as np

df = pd.read_csv("Sales_Funnel_CRM.csv")

print(df)
licenses = df[["Company","Product","Licenses"]]
print(licenses)
print(pd.pivot(data=licenses,index="Company",columns="Product",values="Licenses"))
a = pd.pivot(data=licenses,index="Company",columns="Product",values="Licenses")
print(a.iloc[0])
print(a.iloc[0].name)
a.iloc[0].name = 1
print(a)
b = pd.pivot_table(df,index="Company",aggfunc="sum")
print(b)
print(df.groupby("Company").sum())
c = pd.pivot_table(df,index="Company",aggfunc="sum",values=["Licenses","Sale Price"])
print(c)
d = pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],aggfunc="sum",fill_value=0)
print(d)
e = pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],aggfunc=[np.sum,np.mean],fill_value=0)
print(e)
f = pd.pivot_table(df,index=["Account Manager","Contact","Product"],values=["Sale Price"],aggfunc=[np.sum,np.mean],fill_value=0)
g =  pd.pivot_table(df,index=["Account Manager","Contact","Product"],values=["Sale Price"],aggfunc=[np.sum],fill_value=0,margins=True)
print(g)