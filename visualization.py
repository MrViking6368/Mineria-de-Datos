
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
from plotly.subplots import make_subplots 
warnings.filterwarnings("ignore")
print("The modules are imported")

df=pd.read_csv("vgsales.csv")
df.head()

x=(df['NA_Sales'].mean()*1000000)
y=(df['EU_Sales'].mean()*1000000)
z=(df['JP_Sales'].mean()*1000000)
q=(df['Other_Sales'].mean()*1000000)
p=(df['Global_Sales'].mean()*1000000)

print("Venta promedio en Norte America =", (f"${x:,.3f}")) 
print("Venta promedio en Europa =",(f"${y:,.3f}"))
print("Venta promedio en Japon =",(f"${z:,.3f}"))
print("Venta promedio en otras regiones =",(f"${q:,.3f}"))
print("Venta promedio globales =",(f"${p:,.3f}"))

colors = ['lightslategray',] * 4
colors[1]='darkgray'
colors[2]='grey'
colors[3]='dimgrey'
colors[0] = 'crimson'

bar1 = go.Figure(data=[go.Bar(
    y=['Global','North America', 'Europe', 'Japan',
       'Other'],
    x=[537440.656,264667.430, 146652.006, 77781.660, 48063.020],
    orientation='h',
    marker_color=colors # color del marcador puede ser un solo valor de color o iterable
)])
bar1.update_layout(title_text='Region with highest sales on an average')
bar1.update_xaxes(title='Average Sales')
bar1.update_yaxes(title='Regions')
bar1.show()

#Agrupar ventas norteamericanas basado en cada plataforma
data2 = pd.DataFrame(df.groupby("Platform")[["NA_Sales"]].sum().sort_values(by=['NA_Sales'],ascending=[False]).reset_index())
data2.rename(columns = {'Platform':'Platform_NA'}, inplace = True)

#Agrupar ventas europeas basadas en cada plataforma
data3 = pd.DataFrame(df.groupby("Platform")[["EU_Sales"]].sum().sort_values(by=['EU_Sales'],ascending=[False]).reset_index())
data3.rename(columns = {'Platform':'Platform_EU'}, inplace = True)

#Agrupar ventas japonesas basadas en cada plataforma
data4 = pd.DataFrame(df.groupby("Platform")[["JP_Sales"]].sum().sort_values(by=['JP_Sales'],ascending=[False]).reset_index())
data4.rename(columns = {'Platform':'Platform_JP'}, inplace = True)

#Agrupar ventas de otras regiones basadas en cada plataforma
data5 = pd.DataFrame(df.groupby("Platform")[["Other_Sales"]].sum().sort_values(by=['Other_Sales'],ascending=[False]).reset_index())
data5.rename(columns = {'Platform':'Platform_other'}, inplace = True)

data=pd.concat([data2,data3,data4,data5],axis=1)
data.head(3)

subplot1 = make_subplots(rows=4, cols=1, shared_yaxes=True,subplot_titles=("North American top platforms","Europe top platforms","Japan top platforms","Other regions top platforms"))

subplot1.add_trace(go.Bar(x=data['Platform_NA'], y=data['NA_Sales'],
                    marker=dict(color=[1, 2, 3],coloraxis="coloraxis")),1, 1)

subplot1.add_trace(go.Bar(x=data['Platform_EU'], y=data['EU_Sales'],
                    marker=dict(color=[4, 5, 6], coloraxis="coloraxis")),                         2, 1)
                   
subplot1.add_trace(go.Bar(x=data['Platform_JP'], y=data['JP_Sales'],
                    marker=dict(color=[7, 8, 9], coloraxis="coloraxis")),
                    3, 1)

subplot1.add_trace(go.Bar(x=data['Platform_other'], y=data['Other_Sales'],
                    marker=dict(color=[10, 11, 12], coloraxis="coloraxis")),
                   4, 1)
                   
subplot1.update_layout(height=900,width=500,coloraxis=dict(colorscale='Magenta'), showlegend=False)
subplot1.show()

top = pd.DataFrame(df.groupby("Name")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index())
top.head(10) 

pie1 = px.pie(top, values=top['Global_Sales'][:10], names=top['Name'][:10],title='Top 10 games globally', 
              color_discrete_sequence=px.colors.sequential.Purp_r)
pie1.update_traces(textposition='inside', textinfo='percent+label',showlegend=False)
pie1.show()

genre_df = df.groupby("Genre")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index()
bar_genre= px.bar(genre_df, x='Genre', y='Global_Sales',color='Global_Sales',color_continuous_scale='Burgyl')
bar_genre.show()

