
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

missing_value=['0', 'NaN', np.nan]
df = pd.read_csv('vgsales.csv', na_values=missing_value)
df = df.dropna(axis='index', how='any', subset=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])
df = df.dropna(axis='index', how='any', subset=['Year']) 

# Atributos clustering
features = ['Global_Sales', 'EU_Sales']
data = df[features]

# Normalizar datos
data_norm = (data - data.mean()) / data.std()

#modelo k-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_norm)
df['Cluster'] = kmeans.labels_

plt.scatter(df['Global_Sales'], df['EU_Sales'], c=df['Cluster'])
plt.xlabel('Global_Sales')
plt.ylabel('EU_Sales')
plt.title('Video Game Sales Clustering')
plt.show()
