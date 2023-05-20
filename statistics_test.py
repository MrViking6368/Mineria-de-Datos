import numpy as np
import pandas as pd
from scipy import stats

missing_value=['0', 'NaN', np.nan]
df= pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df= df.dropna(axis='index', how='any', subset=['Year'])

mean1 = df['Global_Sales'].mean()
sum1 = df['Global_Sales'].sum()
max1 = df['Global_Sales'].max()
min1 = df['Global_Sales'].min()
count1 = df['Global_Sales'].count()
median1 = df['Global_Sales'].median() 
std1 = df['Global_Sales'].std() 
var1 = df['Global_Sales'].var()

print('Promedio ventas: ' + str(mean1))
print('Suma ventas: ' + str(sum1))
print('Ventas maximas: ' + str(max1))
print('Ventas minimas: ' + str(min1))
print('Conteo ventas: ' + str(count1))
print('Media ventas: ' + str(median1))
print('std de ventas: ' + str(std1))
print('varianza de ventas: ' + str(var1))

EA = df[(df['Publisher'] == 'Electronic_Arts')]
Acti = df[(df['Publisher'] == 'Activision')]
# homogeniedad
print(stats.levene(EA['Global_Sales'], Acti['Global_Sales']))
#t-test
print(stats.ttest_ind(EA['Global_Sales'], Acti['Global_Sales']))