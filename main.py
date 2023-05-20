import numpy as np
import pandas as pd

missing_value=['0', 'NaN', np.nan]
df= pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df= df.dropna(axis='index', how='any', subset=['Year'])

print(df.isnull().sum())
print(df.tail())
print(df.head())