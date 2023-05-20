#%%
import numpy as np
import pandas as pd
import numbers
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from tabulate import tabulate

missing_value=['0', 'NaN', np.nan]
df = pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df = df.dropna(axis='index', how='any', subset=['Year'])

linear_model = smf.ols(formula= 'Global_Sales~Platform', data = df).fit() 
#print(linear_model.params)
#print(linear_model.pvalues)
#print(linear_model.rsquared)

sales_pred = linear_model.predict(pd.DataFrame(df['Platform']))
print(sales_pred)

print(df.plot(kind='scatter', x='Platform', y='Global_Sales'))
plt.plot(df['Platform'], sales_pred, color= 'red')
plt.xticks(rotation=90)
# %%
