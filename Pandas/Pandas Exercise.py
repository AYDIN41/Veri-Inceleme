import pandas as pd
import numpy as np

hotels = pd.read_csv("hotel_booking_data.csv")
"1"
print(len(hotels))
"2"
print(hotels.isnull().sum())
"3"
print(hotels.drop("company",axis=1))
"4"
print(hotels.info())
#print(hotels["country"])
print(hotels["country"].value_counts().iloc[0:5])
"5"
print(hotels["adr"].max())
print(hotels[hotels["adr"].isin([5400.0])].iloc[0][32])
print(hotels.sort_values('adr',ascending=False)[['adr','name']].iloc[0])
"6"
print(round(hotels["adr"].mean(),2))
"7"
a = hotels["stays_in_week_nights"] + hotels["stays_in_weekend_nights"]
print(round(a.mean(),2))
"8"
def adrForEachNight(adr,weekendNight,weeknight):
    x = weekendNight + weeknight
    return adr * x
hotels["Mean of Money"] =  hotels[["adr","stays_in_weekend_nights","stays_in_week_nights"]].apply(lambda a:adrForEachNight(a["adr"],a["stays_in_weekend_nights"],a["stays_in_week_nights"]),axis=1)
print(round(hotels["Mean of Money"].mean()),2)
"9"
print(hotels[hotels["total_of_special_requests"] == 5][["email","name"]])
"10"
print(hotels["is_repeated_guest"].mean()*100)
"11"


"12"
def totalKid(child,baby):
    return child + baby
hotels["totalKids"] = hotels[["children","babies"]].apply(lambda a:totalKid(a["children"],a["babies"]),axis=1)
print(hotels["totalKids"])
#print(hotels[hotels["totalKids"]>=9.0][["name","adults","totalKids","babies","children"]])
print(hotels.sort_values("totalKids",ascending=False)[["name","adults","totalKids","babies","children"]].iloc[:3])
"13"
print(hotels["arrival_date_day_of_month"].value_counts(sort=False).iloc[0:15].sum())
"14 Yapamadığım"

print(hotels["phone-number"].apply(lambda num:num[0:3]).value_counts()[0:3])

"11 Yapamadığım"

print(hotels['name'].apply(lambda name: name.split()[1]).value_counts()[:5])

"Zor Soru Cevabı"

def convert(day,month,year):
    return f"{day}-{month}-{year}"
hotels["date"] = np.vectorize(convert)(hotels["arrival_date_day_of_month"],hotels["arrival_date_month"],hotels["arrival_date_year"])
hotels["date"] = pd.to_datetime(hotels["date"])
print(hotels["date"])
print(hotels["date"].dt.day_name())
print(hotels["date"].dt.day_name().value_counts())