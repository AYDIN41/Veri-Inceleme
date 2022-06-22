import pandas as pd

df = pd.read_html("https://en.wikipedia.org/wiki/World_population#:~:text=In%20demographics%2C%20the%20term%20world,billion%20as%20of%20November%202021.")
print(len(df))
print(df[0].info())
dfMostPop = df[0].set_index("Most populous countries")
print("Most Population in 2015 ",dfMostPop["2015"])
i = 0
"""while(i<10):
    print("Number of Pop: ",dfMostPop["2015"][i])
    i += 1"""
#print(df[0].dropna(thresh=1))
print(df[0].drop([1,2]))
print(df[0].drop(11))
df[0] = df[0].drop(11)
df[0] = df[0].set_index("#")
print(df[0])
df[0].columns = ["Country","2000","2015","2030 Est."]
print(df[0])
row = df[0].iloc[0]
pd.set_option('chained',None)
df[0].loc["1"].iloc[0] = "China"
print(df[0].loc["1"].iloc[0])

print(df[0])

print(df[6])
df[6] =  df[6].set_index("Rank")
print(df[6])
df[0].to_html("C:\\Users\\asus\\Desktop\\sample.html")