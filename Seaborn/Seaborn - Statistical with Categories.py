import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dm_office_sales.csv")

print(df["division"].value_counts())
print(df.head())
plt.figure(figsize=(10,5))
#sns.countplot(data = df,x = "division")
#plt.ylim(0,10000) #If we would use ylim for countplot there will be deceipt and we do not want to take it
#Best way to display countplot use what countplot to us
sns.set(style="darkgrid")
sns.countplot(data = df,x = "division",hue = "level of education",palette = "turbo")
print(df["level of education"].value_counts())
plt.figure(figsize=(15,5))
print(sns.barplot(data=df,x="level of education",y = "salary",estimator = np.mean,ci="sd"
                  ,hue="division"
                  ))
#plt.legend(loc=(1,0.5))
plt.legend(bbox_to_anchor=(1,1)) #Last of two lines that we came as far are same


plt.show()