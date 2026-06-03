# K-Means Clustering pada Dataset GPS Trajectories

## Deskripsi Proyek

Proyek ini merupakan implementasi algoritma K-Means Clustering menggunakan dataset GPS Trajectories dari UCI Machine Learning Repository. Tujuan dari proyek ini adalah mengelompokkan data perjalanan berdasarkan karakteristik tertentu seperti jarak tempuh (*distance*) dan kecepatan (*speed*).

## Dataset

Dataset yang digunakan berasal dari UCI Machine Learning Repository:

* Dataset: GPS Trajectories
* Sumber: https://archive.ics.uci.edu/dataset/354/gps+trajectories

File yang digunakan:

```text
go_track_tracks.csv
```

## Library yang Digunakan

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
```

## Tahapan Pengerjaan

### 1. Membaca Dataset

Dataset dibaca menggunakan library Pandas dan dikonversi menjadi DataFrame.

```python
baca = pd.read_csv("go_track_tracks.csv")
baca.head()
```

### 2. Melihat Informasi Dataset

Melihat struktur data, jumlah kolom, tipe data, dan jumlah data.

```python
baca.info()
```

### 3. Menghapus Kolom yang Tidak Digunakan

Kolom `linha` dihapus karena tidak digunakan dalam proses clustering.

```python
baca = baca.drop(["linha"], axis=1)
```

### 4. Memilih Variabel Clustering

Variabel yang digunakan:

* distance
* speed

```python
baca_x = baca.iloc[:,1:3]
```

### 5. Visualisasi Persebaran Data

Visualisasi dilakukan untuk melihat pola persebaran data sebelum clustering.

```python
plt.scatter(
    baca.distance,
    baca.speed
)
plt.show()
```

### 6. Mengubah Data Menjadi Array

Data DataFrame dikonversi menjadi array NumPy.

```python
x_array = np.array(baca_x)
```

### 7. Normalisasi Data

Normalisasi dilakukan menggunakan Min-Max Scaling agar seluruh fitur berada pada rentang yang sama.

```python
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)
```

### 8. Pembuatan Model K-Means

Model K-Means dibuat dengan jumlah cluster sebanyak 3.

```python
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(x_scaled)
```

### 9. Menambahkan Label Cluster

Hasil cluster ditambahkan ke dalam dataset.

```python
baca["cluster"] = kmeans.labels_
```

### 10. Visualisasi Hasil Clustering

Visualisasi cluster dan centroid hasil K-Means.

```python
plt.scatter(
    x_scaled[:,0],
    x_scaled[:,1],
    c=kmeans.labels_
)
```

## Dokumentasi

### Figure 1 - Informasi Dataset

![Figure 1](figure1.png)

Keterangan:

Menampilkan informasi dataset menggunakan fungsi `info()` untuk mengetahui jumlah data, tipe data, dan struktur dataset.

### Figure 2 - Visualisasi Hasil Clustering

![Figure 2](figure2.png)

Keterangan:

Menampilkan hasil pengelompokan data menggunakan algoritma K-Means Clustering beserta centroid masing-masing cluster.

## Hasil

Berdasarkan proses clustering menggunakan algoritma K-Means, data perjalanan berhasil dikelompokkan ke dalam tiga cluster berdasarkan kemiripan karakteristik perjalanan. Hasil clustering dapat digunakan untuk menganalisis pola perjalanan pengguna berdasarkan jarak dan kecepatan.

## Kesimpulan

Algoritma K-Means Clustering berhasil diterapkan pada dataset GPS Trajectories. Dengan melakukan normalisasi data dan pengelompokan berdasarkan fitur yang dipilih, diperoleh beberapa kelompok data yang memiliki karakteristik perjalanan yang serupa.
