import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("dm_office_sales.csv")

print(df.head())

print(df.info())
plt.figure(figsize=(12,4),dpi=150)
#sns.scatterplot(x = "salary",y = "sales",data = df,hue="level of education",palette = "Set2")
#Seaborn ile başka bir column ile görseli nasıl işleyeceğimiz ve görsellik katacağımızı görüyoruz
#sns.scatterplot(x = "salary",y = "sales",data = df,hue="salary",palette = "inferno")
#seaborn ile y veya x eksenleri ile aynı veri tipini kullanarak nasıl işlem yapılacağı görülüyor

#sns.scatterplot(x = "salary",y = "sales",data = df,size = "salary")

#sns.scatterplot(x = "salary",y = "sales",data = df,size = "work experience")

#sns.scatterplot(x = "salary",y = "sales",data = df,s = 200,alpha = 0.3)
# Alpha fonksiyonu ile transparan bir görünüm sağlıyoruz

#sns.scatterplot(x = "salary",y="sales",data = df,s = 200,style = "level of education")
#sns.scatterplot(x = "salary",y = "sales",data = df,hue="salary",palette = "inferno")
sns.scatterplot(x= "salary",y="sales",data = df,hue="level of education",style = "level of education",s = 200,alpha = 0.9)
plt.savefig("firstTrial.png")
plt.show()
