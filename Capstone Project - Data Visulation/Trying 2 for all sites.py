
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fandango = pd.read_csv("fandango_scrape.csv")
newDf = fandango[fandango["VOTES"]>0]

all_sites = pd.read_csv("all_sites_scores.csv")

newDf["DIFF"] = newDf["STARS"] - newDf["RATING"]
newDf["DIFF"] = newDf["DIFF"].round(2)

print(all_sites.info())
print(all_sites.columns)
print(all_sites.describe())
sns.scatterplot(data=all_sites,x="RottenTomatoes_User",y="RottenTomatoes")
all_sites["Rotten_Diff"] = all_sites["RottenTomatoes"] - all_sites["RottenTomatoes_User"]
print(all_sites["Rotten_Diff"])
print(all_sites["Rotten_Diff"].apply(abs).mean())
plt.figure(figsize=(12,6))
#all_sites["AbsRottenDiff"] = all_sites["Rotten_Diff"].abs()
#print(all_sites["AbsRottenDiff"])
#sns.histplot(data=all_sites,x="AbsRottenDiff",kde=True,bins=25)
sns.histplot(x=all_sites["Rotten_Diff"].apply(abs),kde=True,bins=25)
plt.title("Abs Difference between RT Critics Score and RT User Score")
print(all_sites.nsmallest(5,"Rotten_Diff"))
print(all_sites.nlargest(5,"Rotten_Diff"))
sns.displot(data=all_sites,x="Rotten_Diff",kde=True)

sns.scatterplot(data=all_sites,x="Metacritic",y="Metacritic_User")

sns.scatterplot(data=all_sites,x="IMDB_user_vote_count",y="Metacritic_user_vote_count")

print(all_sites["IMDB_user_vote_count"].max())

combineDataFrame = pd.merge(left=fandango,right=all_sites,how="inner")

combineDataFrame["NormIMDB"] = combineDataFrame["IMDB"] / 2
combineDataFrame["NormRTC"] = combineDataFrame["RottenTomatoes"] / 20
combineDataFrame["NormRTUsers"] = combineDataFrame["RottenTomatoes_User"] / 20
combineDataFrame["NMeC"] = combineDataFrame["Metacritic"] / 20
combineDataFrame["NormMUser"] = combineDataFrame["Metacritic_User"] / 2

NormScores = combineDataFrame[["STARS","RATING","NormIMDB","NormRTC","NormRTUsers","NMeC","NormMUser"]]
NormScores.head()



print(combineDataFrame["NormalizeIMDB"])
print(combineDataFrame["NormalizeRottenTomatoesCrities"])
print(combineDataFrame["NormalizeRottenTomatoesUsers"])
print(combineDataFrame["NormalizeMetacritic"])
print(combineDataFrame["NormalizeMetacritic_User"])


# CODE HERE
def move_legend(
        ax,
        new_loc,
        **kws):
    old_legend = ax.legend_
    handles = old_legend.legendHandles
    labels = [
        t.get_text()
        for
        t
        in
        old_legend.get_texts()]
    title = old_legend.get_title().get_text()
    ax.legend(
        handles,
        labels,
        loc=new_loc,
        title=title,
        **kws)


fig, ax = plt.subplots(
    figsize=(
    10,
    5),
    dpi=150)
sns.kdeplot(
    data=NormScores,
    clip=[
        0,
        5],
    shade=True,
    palette="Set1",
    ax=ax)
move_legend(
    ax,
    "upper left")


plt.figure(figsize=(15,6))
sns.kdeplot(data=NormScores[["STARS","NormRTC"]],fill=True,clip=[0,5])

plt.figure(figsize=(17,6))
sns.histplot(data=NormScores,bins=45)

NormScores = NormScores.drop(columns="FILM")
sns.clustermap(NormScores,cmap='magma',col_cluster=False)

NormScores["FILM"] = combineDataFrame["FILM"]


NormScores.nsmallest(10,"NormRTC")

a = NormScores.nsmallest(10,"NormRTC")


a = NormScores.nsmallest(10,"NormRTC")
plt.figure(figsize=(15,6))
sns.kdeplot(data = a,shade = True,palette = "viridis")

a = NormScores[NormScores["FILM"] == "Taken 3 (2015)"]
print(a)

plt.show()