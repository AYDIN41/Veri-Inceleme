import pandas as pd
import numpy as np
from sqlalchemy import create_engine

tempDb = create_engine("sqlite:///:memory:")
#simpleData = pd.DataFrame(data=np.random.randint(low=0,high=100,size=(4,4)),columns=["A","B","C","D"])
a = np.arange(1,17)
a = a.reshape(4,4)
simpleData = pd.DataFrame(data=a,columns=["A","B","C","D"])
print(simpleData)

simpleData.to_sql(name="newTable",con=tempDb,index=False)
#simpleData.to_sql(name="newTable",con=tempDb,if_exists="replace") #Var olan bir database'in üstüne oberwrite ,işem, gerçekleştiriyoruz
c = pd.read_sql(sql="newTable",con=tempDb,index_col=False)
print(c)

d = pd.read_sql_query(sql="SELECT * From newTable",con=tempDb)
print(d)
result = pd.read_sql_query(sql="SELECT a,d From newTable",con=tempDb)
print(result)
