import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Bobo','Yolanda','Andrew']})

print(pd.merge(registrations,logins,how="outer",on="name"))

registrations = registrations.set_index("name")
print(registrations)
print(pd.merge(registrations,logins,left_index=True,right_on="name",how="inner"))
registrations = registrations.reset_index()
print(registrations)
registrations.columns = ["reg_name","reg_id"]
print(registrations)

print(pd.merge(registrations,logins,left_on="reg_name",right_on="name",how="inner"))
registrations.columns = ["name","id"]
print(logins)
logins.columns = ["id","name"]
print(logins)

print(pd.merge(registrations,logins,how="inner",on="name")) #Pandas aynı isimden değişkenleri otomatik olarak x ve y gibi ek isimle adlandırıyor
print(pd.merge(registrations,logins,how="inner",on="name",suffixes=("_reg","_log")))
