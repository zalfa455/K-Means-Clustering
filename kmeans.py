import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

baca = pd.read_csv("go_track_tracks.csv")
baca.head()
baca.info() 
baca = baca.drop(["linha"], axis=1) 
baca.head()

baca_x = baca.iloc[:, 1:3] 
baca_x.head()

x_array = np.array(baca_x) 
print(x_array) 
scaler = MinMaxScaler() 
x_scaled = scaler.fit_transform(x_array) 
x_scaled

from sklearn.cluster import KMeans 
# Membuat model KMeans 
kmeans = KMeans(n_clusters=3, random_state=42) 
# Training model 
kmeans.fit(baca) 
# Menampilkan label cluster 
print(kmeans.labels_) 
# Menambahkan hasil cluster ke dataframe 
baca["kluster"] = kmeans.labels_ 
4 
# Menampilkan data 
print(baca.head())

# Plot hasil clustering 
plt.figure(figsize=(8,6)) 
 
plt.scatter( 
    baca['id_android'], 
    baca['speed'], 
    c=baca['kluster'], 
    cmap='viridis' 
) 
 
# Titik centroid 
plt.scatter( 
    kmeans.cluster_centers_[:, 1],   # Frequency 
    kmeans.cluster_centers_[:, 2],   # Monetary 
    s=200, 
    c='red', 
    marker='X', 
    label='Centroid' 
) 
 
plt.xlabel('Frequency') 
plt.ylabel('Monetary') 
plt.title('K-Means Clustering') 
plt.legend() 
 
plt.show()