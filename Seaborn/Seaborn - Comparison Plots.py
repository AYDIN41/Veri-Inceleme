import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())

#sns.jointplot(data=df,x = "math score",y = "reading score",kind="hist")

#sns.jointplot(data=df,x = "math score",y = "reading score",kind="kde",shade=True)

sns.jointplot(data=df,x="math score",y="reading score",hue="gender")

#sns.pairplot(data=df,hue = "gender")

#sns.pairplot(data=df,hue = "gender",diag_kind = "hist")

sns.pairplot(data=df,corner=True,hue="gender",palette = "terrain")

plt.show()