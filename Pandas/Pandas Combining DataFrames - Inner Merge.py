import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Bobo','Yolanda','Andrew']})

print(registrations)
print(logins)

print(pd.merge(registrations,logins,how="inner",on="name"))
print(pd.merge(logins,registrations,how="inner",on="name"))

"""
Left and Right method on combining dataFrame
"""

print(pd.merge(left=registrations,right=logins,how="left",on="name"))
print(pd.merge(left=registrations,right=logins,how="right",on="name"))