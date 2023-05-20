import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

missing_value=['0', 'NaN', np.nan]
df = pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df = df.dropna(axis='index', how='any', subset=['Year']) 

features = ['Global_Sales', 'EU_Sales']
target = 'Genre'

X = df[features]
y = df[target]

# Normalizar
scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

# modelo k-NN 
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_normalized, y)

predictions = knn.predict(X_normalized)

plt.scatter(df['Global_Sales'], df['EU_Sales'], c='blue')
plt.xlabel('Global Sales')
plt.ylabel('EU_Sales')
plt.title('Video Game Sales Classification')
plt.show()