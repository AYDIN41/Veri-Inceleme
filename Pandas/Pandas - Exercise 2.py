import pandas as pd

df = pd.read_csv("Salaries.csv")

print(df.head())

print(df.info())

print(df["BasePay"].mean())

print(df["OvertimePay"].max())

print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"].iloc[0][2])

print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"].iloc[0][7])

print(df[df["TotalPay"] == df["TotalPay"].max()])

print(df[df["TotalPay"] == df["TotalPay"].min()])

print(df.info())
print(df.groupby("Year").mean()["BasePay"])

print(df["JobTitle"].nunique())

print(df["JobTitle"].value_counts()[:5])

print(sum(df[df["Year"] == 2013 ]["JobTitle"].value_counts() == 1))

#print(df[df["JobTitle"].isin(["Chief"])]) Yanlış

#Doğru

def chiefStr(name):
    if "chief" in name.lower():
        return True
    else:
        return False
print(sum(df["JobTitle"].apply(lambda a : chiefStr(a))))

#print(df.corr(method="pearson")[["TotalPayBenefits",len(df["Id"])]]) Yanlış

df["title_len"] = df['JobTitle'].apply(len)
print(df[["title_len","TotalPayBenefits"]].corr())