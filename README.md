# K-Means Clustering pada Dataset GPS Trajectories dan TLC New Driver Application Status

## Deskripsi

Proyek ini merupakan implementasi algoritma K-Means Clustering pada dua dataset yang berbeda, yaitu GPS Trajectories dan TLC New Driver Application Status. Tujuan dari proyek ini adalah mempelajari penerapan algoritma K-Means untuk mengelompokkan data berdasarkan karakteristik yang dimiliki sehingga data yang memiliki kemiripan dapat berada pada cluster yang sama.

## Dataset

### Dataset 1: GPS Trajectories

Dataset ini berisi informasi perjalanan yang direkam menggunakan GPS.

* Nama Dataset : GPS Trajectories
* Sumber : UCI Machine Learning Repository

File yang digunakan:

```text
go_track_tracks.csv
```

Fitur yang digunakan:

* Distance
* Speed

---

### Dataset 2: TLC New Driver Application Status

Dataset ini berisi informasi status pengajuan calon pengemudi.

* Nama Dataset : TLC New Driver Application Status
* Sumber : Kaggle

File yang digunakan:

```text
TLC_New_Driver_Application_Status.csv
```

Fitur yang digunakan:

* Type
* Status

## Library yang Digunakan

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
```

## Tahapan Pengerjaan

### 1. Import Library

Mengimpor library yang diperlukan untuk proses clustering.

### 2. Membaca Dataset

Dataset dibaca menggunakan Pandas dan dikonversi menjadi DataFrame.

### 3. Data Cleaning

* Dataset GPS Trajectories: menghapus kolom yang tidak digunakan.
* Dataset TLC: menghapus kolom App No.

### 4. Data Preprocessing

* Dataset GPS Trajectories menggunakan data numerik secara langsung.
* Dataset TLC menggunakan Label Encoding untuk mengubah data kategorikal menjadi numerik.

### 5. Konversi Data ke Array

Data yang digunakan untuk clustering dikonversi menjadi array NumPy.

### 6. Normalisasi Data

Normalisasi dilakukan menggunakan Min-Max Scaling.

### 7. Penentuan Jumlah Cluster

Jumlah cluster ditentukan menggunakan metode Elbow.

### 8. Pembuatan dan Pelatihan Model K-Means

Model K-Means dilatih menggunakan data yang telah dinormalisasi.

### 9. Hasil Clustering

Data berhasil dikelompokkan ke dalam beberapa cluster berdasarkan karakteristik masing-masing dataset.

## Dokumentasi

### Dataset GPS Trajectories

#### Figure 1 - Dataset Awal

Menampilkan data sebelum proses clustering dilakukan.

#### Figure 2 - Informasi Dataset

Menampilkan struktur dan tipe data dataset.

#### Figure 3 - Data Setelah Preprocessing

Menampilkan data yang telah dibersihkan dan siap diproses.

#### Figure 4 - Konversi ke Array

Menampilkan hasil konversi data ke array NumPy.

#### Figure 5 - Hasil Evaluasi

Menampilkan hasil clustering dan evaluasi model.

---

### Dataset TLC New Driver Application Status

#### Figure 1 - Dataset Awal

Menampilkan visualisasi data sebelum clustering.

#### Figure 2 - Informasi Dataset

Menampilkan struktur dataset dan tipe data.

#### Figure 3 - Data Setelah Encoding

Menampilkan hasil Label Encoding pada seluruh atribut kategorikal.

#### Figure 4 - Hasil Clustering

Menampilkan hasil pengelompokan data menggunakan K-Means beserta centroid.

#### Figure 5 - Jumlah Data Tiap Cluster

Menampilkan distribusi jumlah data pada masing-masing cluster.

## Hasil

Implementasi K-Means Clustering berhasil diterapkan pada kedua dataset. Hasil clustering menunjukkan bahwa data dapat dikelompokkan berdasarkan karakteristik yang serupa sehingga memudahkan proses analisis dan interpretasi data.

## Kesimpulan

Algoritma K-Means Clustering berhasil diterapkan pada dataset GPS Trajectories dan TLC New Driver Application Status. Meskipun kedua dataset memiliki karakteristik yang berbeda, proses preprocessing dan clustering mampu menghasilkan kelompok data yang dapat digunakan untuk analisis lebih lanjut.

## Author

Nama : Nazwa Zalfa

Mata Kuliah : Pembelajaran Mesin
