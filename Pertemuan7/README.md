🧠 Pertemuan 7 - Jaringan Syaraf Tiruan (Deep Learning)

Repositori ini berisi hasil pengerjaan modul Praktikum Kecerdasan Buatan (KB) Pertemuan 7 yang berfokus pada klasifikasi multi-kelas menggunakan arsitektur Jaringan Syaraf Tiruan (JST) yang lebih dalam (*Deep Neural Network*). Praktikum ini diimplementasikan menggunakan *framework* modern **TensorFlow** dan **Keras** untuk mengenali berbagai jenis spesies bunga.

📁 Struktur Folder

* `Pertemuan7/`
  * `main1.ipynb` (Notebook Eksperimen & Analisis)
  * `main.py` (Skrip Utama Aplikasi)
  * `iris.data` (Dataset Lokal Spesies Iris)
  * `README.md` (Dokumentasi Teknis)

🛠️ Studi Kasus: Klasifikasi Spesies Bunga Iris

Aplikasi ini dirancang untuk memprediksi 3 varietas bunga Iris (*Iris-setosa*, *Iris-versicolor*, dan *Iris-virginica*) berdasarkan 4 karakteristik fisik tanaman, yaitu panjang dan lebar sepal, serta panjang dan lebar petal.

### 📊 Dataset & Pra-pemrosesan
Dataset yang digunakan diambil dari *UCI Machine Learning Repository* (`iris.data`). Sebelum dimasukkan ke dalam model, data melalui tahap pra-pemrosesan berikut:
1. **Label Encoding:** Mengubah target kategori string menjadi bentuk numerik.
2. **Feature Scaling:** Normalisasi data fitur agar proses *training* JST berjalan lebih stabil dan konvergen.

⚙️ Arsitektur Deep Neural Network

Model yang dibangun merupakan *Multi-Layer Perceptron* (MLP) dengan struktur lapisan yang cukup padat untuk mengekstrak pola fitur secara optimal:

| Lapisan (Layer) | Jenis Layer | Spesifikasi & Aktivasi |
| :--- | :--- | :--- |
| **Lapisan Input** | Input Layer | shape=(4,) (Menampung 4 fitur Iris) |
| **Hidden Layer 1** | Dense (Fully Connected) | 1000 units, Aktivasi **ReLU** |
| **Hidden Layer 2** | Dense (Fully Connected) | 500 units, Aktivasi **ReLU** |
| **Hidden Layer 3** | Dense (Fully Connected) | 300 units, Aktivasi **ReLU** |
| **Lapisan Output** | Dense (Fully Connected) | 3 units, Aktivasi **Softmax** (Probabilitas Kelas) |

📊 Hasil Praktikum

Program ini dikonfigurasi menggunakan fungsi kehilangan *Loss Function* berbasis **Categorical Crossentropy** untuk mengukur tingkat eror klasifikasi multi-kelas.

* **Proses Training:** Model dilatih untuk mengenali pola data latih dengan mengoptimasi bobot (*weights*) dan bias di setiap epoch.
* **Metrik Evaluasi:** Keberhasilan model dipantau melalui grafik pergerakan akurasi (*Accuracy*) serta penurunan nilai *Loss* yang divisualisasikan menggunakan pustaka grafik Python.

🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat (Prerequisites)
Pastikan lingkungan lokal kamu sudah terinstal pustaka berikut:
* Python 3.x
* Framework: `tensorflow` (Keras)
* Data Science Tools: `numpy`, `pandas`, `scikit-learn`
* Visualisasi: `matplotlib`, `seaborn`

### 2. Langkah Menjalankan Program
1. Salin (*clone*) atau unduh repositori praktikum ini ke komputer kamu.
2. Buka terminal atau Command Prompt (CMD), lalu arahkan ke direktori proyek ini:
   ```bash
   cd Pertemuan7
   ```
