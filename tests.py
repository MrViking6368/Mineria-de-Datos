import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols 

missing_value=['0', 'NaN', np.nan]
df = pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df = df.dropna(axis='index', how='any', subset=['Year'])

mod = ols('Global_Sales~Platform', data = df).fit()
aov = sm.stats.anova_lm(mod, type=2)
print(aov)

mod1 = ols('Global_Sales~Platform+Publisher', data = df).fit()
aov1 = sm.stats.anova_lm(mod1, type=2)
print(aov1)