import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_table.csv")

df = df.set_index("Countries")

#sns.heatmap(df)
plt.figure(dpi=200)
sns.heatmap(df.drop("Life expectancy",axis=1),linewidth = 0.5,annot=True,
            cmap="plasma")

sns.clustermap(df.drop("Life expectancy",axis=1),linewidth = 0.5,annot=True,
            cmap="plasma",col_cluster=False)

plt.show()