import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("application_record.csv")

print(df.head())
"""

employee = df[df["DAYS_EMPLOYED"]<0]

employee["DAYS_EMPLOYED"] = -1*employee["DAYS_EMPLOYED"]
employee["DAYS_BIRTH"] = -1*employee["DAYS_BIRTH"]

sns.scatterplot(data=employee,x="DAYS_BIRTH",y="DAYS_EMPLOYED",alpha=0.01,linewidth = 0)

print(df["DAYS_BIRTH"])

age = -1 * df["DAYS_BIRTH"]
age = age//365
df["Age in Years"] = age
a = df["Age in Years"]
sns.displot(data=df,x="Age in Years",lw=35,color="red")
plt.figure(figsize=(12,8))
bottomHalfIncome = df.nsmallest(n=int(0.5*len(df)),columns="AMT_INCOME_TOTAL")
sns.boxplot(data=bottomHalfIncome,x="NAME_FAMILY_STATUS",y="AMT_INCOME_TOTAL",hue="FLAG_OWN_REALTY")
plt.legend(loc = (1.05,0.5),borderaxespad=0.,title="FLAG_OWN_REALTY")
plt.title("Income Totals per Family Status for Bottom Half of Earners")
"""

df = df.drop("FLAG_MOBIL",axis=1)
df = df.corr()
sns.heatmap(data=df,cmap ="viridis")
plt.show()
