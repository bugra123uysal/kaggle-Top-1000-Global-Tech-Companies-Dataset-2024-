import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("/kaggle/input/top-1000-global-tech-companies-dataset-2024/Top 1000 technology companies.csv")
print(data.columns)
print(data.info())
print(data.isnull().sum())
print()
print()
print()


plt.pie(data['Industry'].value_counts() ,  labels=data['Industry'].unique(), autopct="%1.1f%%", startangle=90 )
plt.show()

tn=data['Industry'].tail(30)
sns.countplot(x=tn)
plt.xticks(rotation=90)
plt.show()


plt.pie(data['Country'].value_counts(), labels=data['Country'].unique(), autopct='%1.1f%%', startangle=90)
plt.show()

b=data['Country'].head(30)
sns.countplot(x=b, data=data)
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

f=data['Country'].tail(30)
sns.countplot(x=f , data=data )
plt.show()


mark=data['Industry'].head(30)
nu=data['Country'].head(30)
sns.countplot(x=nu, hue=mark ,data=data )
plt.xticks(rotation=90)
plt.show()


mr=data['Industry'].tail(30)
vv=data['Country'].tail(30)
sns.countplot(x=vv, hue=mr, data=data)
plt.xticks(rotation=90)
plt.show()



plt.figure(figsize=(10,10))
p=data['Market Cap'].head(30)
pr=data['Country'].head(30)
f=data['Market Cap'].tail(30)
ff=data['Country'].tail(30)
sns.scatterplot(x='Industry' , y=p , hue=pr , data=data)
sns.scatterplot(x='Industry' , y=f , hue=ff , data=data)
plt.xticks(rotation=90)
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left' )
plt.show()


plt.figure(figsize=(10,10))
a=data['Market Cap'].head(30)
b=data['Country'].head(30)
aa=data['Market Cap'].tail(30)
bb=data['Country'].tail(30)
sns.scatterplot( x=b , y=a   ,data=data)
sns.scatterplot(x=bb , y=aa , color="yellow" ,data=data )
plt.xticks(rotation=90)
plt.show('Market Cap')