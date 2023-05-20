import pandas as pd
import numpy as np
import warnings
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import statsmodels.api as sm
#from statsmodels.tsa.arima_model import ARIMA

df = pd.read_csv('vgsales.csv', index_col=['Year'], parse_dates=True) 
missing_value=['0', 'NaN', np.nan]
df = pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df = df.dropna(axis='index', how='any', subset=['Year']) 

def ad_test(dataset):
    dftest= adfuller(dataset, autolag = 'AIC')
    print("1. ADF: ",dftest[0])
    print("2. P-Value: ",dftest[1])
    print("3. Num. lags: ",dftest[2])
    print("4. Num. observacion para regresion adf y calculo valores criticos: ",dftest[4])
    print("5. Valores criticos: ")
    for key, val in dftest[4].items():
        print("/t",key,":", val)

warnings.filterwarnings('ignore')

stepwise_fit= auto_arima(df['Global_Sales'], trace=True,
                        suppress_warnings=True)

stepwise_fit.summary()

print(df.shape)
train=df.iloc[:-30]
test=df.iloc[-30:]
print(train.shape,test.shape)

model=sm.tsa.arima.ARIMA(train['Global_Sales'], order=(1,0,5))
model=model.fit()
model.summary()

start=len(train)
end=len(train)+len(test)-1
pred=model.predict(start=start,end=end,type='levels')
print(pred)

pred.plot(legend=True)
test['Global_Sales'].plot(legend=True)