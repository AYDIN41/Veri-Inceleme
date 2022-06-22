import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())
print(df.info())
plt.figure(figsize=(10,8),dpi=150)
"""sns.boxplot(data=df,y="reading score",x="parental level of education",
            hue = "test preparation course")"""

"""sns.boxplot(data=df,y="parental level of education",x = "reading score",
            hue = "test preparation course",
            palette = "winter")
"""

"""sns.violinplot(data=df,x = "reading score",y="parental level of education",
              hue = "test preparation course",
              palette = "rainbow",split = True,
              inner = None)""" #We can use inner = None that means we can remove box middle of box
"""sns.violinplot(data=df,x = "reading score",y="parental level of education",
              hue = "test preparation course",
              palette = "rainbow",split = True,
              inner = "quartile")""" #We can use inner = "quartile" which means divide our 4 pieces

sns.violinplot(data=df,x = "reading score",y="parental level of education",
              hue = "test preparation course",
              palette = "rainbow",split = True,
              inner = "stick") # We can use inner = "stick"that means divide lots of lines with stick


plt.legend(loc = (1.05,0.5))

plt.figure(figsize=(17,7))
sns.swarmplot(data=df,x="math score",y="gender",s = 8)

plt.figure(figsize=(17,7))
sns.swarmplot(data=df,x="math score",s = 10)

plt.figure(figsize=(17,7))
sns.swarmplot(data=df,x="math score",y="gender",size = 6
              ,hue="test preparation course",dodge=True)


sns.boxenplot(x="math score",y="test preparation course",data=df,
             hue="gender")


plt.show()








