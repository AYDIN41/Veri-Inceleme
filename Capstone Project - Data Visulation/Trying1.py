
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")

print(fandango.head())
print(fandango.info())
print(fandango.describe())

sns.scatterplot(data=fandango,x="RATING",y="VOTES")
print(fandango.corr())
fandango["YEAR"] = fandango["FILM"].apply(lambda title:title.split("(")[-1])
fandango["YEAR"] = fandango["YEAR"].str.replace(")","")
print(fandango["YEAR"].value_counts())
sns.displot(data=fandango,x="YEAR",palette="Reds")

print(fandango.nlargest(10,"VOTES"))
print(fandango[fandango["VOTES"] == 0].count()[3])


newDf = fandango[fandango["VOTES"]>0]

print(newDf)

print(fandango["RATING"])
plt.figure(figsize = (16,6))
sns.kdeplot(data=newDf,x="RATING",clip=[0,5],label="Stars displayed",fill=True)
sns.kdeplot(data=newDf,x="STARS",clip=[0,5],label="True rating",fill=True)
plt.legend(loc=(1.05,0.5),fontsize=15)


newDf["DIFF"] = newDf["STARS"] - newDf["RATING"]
newDf["DIFF"] = newDf["DIFF"].round(2)
print(newDf.head())


plt.figure(figsize=(12,4))
sns.countplot(data=newDf,x="DIFF",palette="magma")

print(newDf[newDf["DIFF"]>=1.0])

plt.show()