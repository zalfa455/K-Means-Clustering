import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# ==========================
# MEMBACA DATASET
# ==========================

baca = pd.read_csv("TLC_New_Driver_Application_Status.csv")

print("=== 5 DATA TERATAS ===")
print(baca.head())

print("\n=== INFORMASI DATASET ===")
print(baca.info())

# ==========================
# HAPUS KOLOM YANG TIDAK DIGUNAKAN
# ==========================

baca = baca.drop(["App No"], axis=1)

# ==================================
# ENCODING DATA KATEGORI MENJADI ANGKA
# ==================================

le = LabelEncoder()

for kolom in baca.columns:
    baca[kolom] = le.fit_transform(baca[kolom].astype(str))

print("\nDATA SETELAH ENCODING")
print(baca.head())

# ==================================
# MEMBUAT ARRAY (SEPERTI DI MODUL)
# ==================================

X = baca[["Type", "Status"]].values

# ==================================
# NORMALISASI
# ==================================

scaler = MinMaxScaler()
X = scaler.fit_transform(X)


# ==========================
# ENCODING DATA KATEGORI
# ==========================

le = LabelEncoder()

for kolom in baca.columns:
    baca[kolom] = le.fit_transform(baca[kolom].astype(str))

print("\n=== DATA SETELAH ENCODING ===")
print(baca.head())

# ==========================
# PILIH 2 FITUR UNTUK VISUALISASI
# ==========================

fitur = ["Type", "Status"]

X_df = baca[fitur]

# ==========================
# NORMALISASI
# ==========================

scaler = MinMaxScaler()
X = scaler.fit_transform(X_df)



# ==========================
# K-MEANS CLUSTERING
# ==========================

kmeans = KMeans(
    n_clusters=3,
    init="k-means++",
    random_state=42
)

cluster = kmeans.fit_predict(X)

# ==========================
# TAMBAHKAN HASIL CLUSTER
# ==========================

baca["Cluster"] = cluster

print("\n=== JUMLAH DATA TIAP CLUSTER ===")
print(baca["Cluster"].value_counts())

# ==========================
# AMBIL CENTROID
# ==========================

centroid = kmeans.cluster_centers_

# ==========================
# VISUALISASI HASIL CLUSTER
# ==========================

plt.figure(figsize=(10, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=cluster,
    cmap="viridis",
    s=30
)

plt.scatter(
    centroid[:, 0],
    centroid[:, 1],
    c="red",
    marker="X",
    s=250,
    label="Centroid"
)

plt.title("K-Means Clustering")
plt.xlabel("Type")
plt.ylabel("Status")
plt.legend()

plt.show()