import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings("ignore")
print("The modules are imported")

df=pd.read_csv("vgsales.csv")
df.head()

x=(df['NA_Sales'].mean()*1000000)
y=(df['EU_Sales'].mean()*1000000)
z=(df['JP_Sales'].mean()*1000000)
q=(df['Other_Sales'].mean()*1000000)
p=(df['Global_Sales'].mean()*1000000)

print("The average sales in North America =", (f"${x:,.3f}")) #comma separated values till 3 decimal place and $ sign
print("The average sales in Europe =",(f"${y:,.3f}"))
print("The average sales in Japan =",(f"${z:,.3f}"))
print("The average sales in other regions =",(f"${q:,.3f}"))
print("The average sales globally =",(f"${p:,.3f}"))

#Grouping the north america sales based on each platform
data2 = pd.DataFrame(df.groupby("Platform")[["NA_Sales"]].sum().sort_values(by=['NA_Sales'],ascending=[False]).reset_index())
data2.rename(columns = {'Platform':'Platform_NA'}, inplace = True)

#Grouping the europe sales based on each platform
data3 = pd.DataFrame(df.groupby("Platform")[["EU_Sales"]].sum().sort_values(by=['EU_Sales'],ascending=[False]).reset_index())
data3.rename(columns = {'Platform':'Platform_EU'}, inplace = True)

#Grouping the japan sales based on each platform
data4 = pd.DataFrame(df.groupby("Platform")[["JP_Sales"]].sum().sort_values(by=['JP_Sales'],ascending=[False]).reset_index())
data4.rename(columns = {'Platform':'Platform_JP'}, inplace = True)

#Grouping the other region sales based on each platform
data5 = pd.DataFrame(df.groupby("Platform")[["Other_Sales"]].sum().sort_values(by=['Other_Sales'],ascending=[False]).reset_index())
data5.rename(columns = {'Platform':'Platform_other'}, inplace = True)

#Concatenating our datasets
data=pd.concat([data2,data3,data4,data5],axis=1)
print(data.head(3))

top = pd.DataFrame(df.groupby("Name")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index())
print(top.head(10)) #Printing the top 10 results