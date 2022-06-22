import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())

sns.catplot(data = df,x="gender",y="math score",kind = "box",row="lunch")
sns.catplot(data = df,x="gender",y="math score",kind = "box",col="lunch")

sns.catplot(data=df,x="gender",y="math score",
           kind = "box", col = "lunch",row = "test preparation course")

sns.catplot(data=df,x="gender",y="math score",kind = "violin",
           col = "lunch",row = "test preparation course")

sns.PairGrid(df)

g = sns.PairGrid(df,hue="gender")

g = g.map_upper(sns.scatterplot)

g = g.map_diag(sns.histplot)

g = g.map_lower(sns.kdeplot)

g = g.add_legend()
