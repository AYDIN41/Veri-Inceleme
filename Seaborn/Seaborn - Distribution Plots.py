import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dm_office_sales.csv")

print(df.head())
#plt.figure(figsize=(5,7),dpi=150)
#sns.rugplot(x="salary",data = df,height=0.25)
#sns.set(style="darkgrid") #In the jupiter notebook,once we set style it will not change even we will make comment line for set line
#sns.set(style="ticks")
#sns.displot(x="salary",data=df,bins=20,color="green",linewidth = 4,edgecolor = "blue",ls=":")
#As we can see,we can use matplotlib features in the seaborn .displot
#sns.histplot(data=df,x= "salary",kde=True,rug=True) #Histplot does not have this featre when we run this we will take an error
#sns.displot(data=df,x="salary",kde=True)

#sns.kdeplot(data=df,x="salary")

np.random.seed(42)
randomNumber = np.random.randint(0,100,200)
print(randomNumber)

randomNumber = pd.DataFrame(randomNumber,columns=["age"])

#sns.rugplot(data=randomNumber,x="age")

sns.displot(data=randomNumber,x="age",rug=True,bins=30)
sns.displot(data=randomNumber,x="age",rug=True,color="green",bins=30,kde=True)
sns.kdeplot(data=randomNumber,x="age",clip=[0,100])
sns.kdeplot(data=randomNumber,x="age",clip=[0,100],bw_adjust=0.3,shade=True)
#When we increase the bandwidth the grapth line will be look like normal distributon line we do not want to see actually

print(randomNumber)

plt.show()

