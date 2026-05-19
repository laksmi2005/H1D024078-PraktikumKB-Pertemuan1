# 🖼️ Pertemuan 8 - Convolutional Neural Network (CNN)

Repositori ini berisi hasil pengerjaan modul Praktikum Kecerdasan Buatan (KB) Pertemuan 8 yang berfokus pada implementasi arsitektur *Convolutional Neural Network* (CNN). Praktikum ini bertujuan untuk memahami ekstraksi fitur spasial pada citra digital serta membangun, melatih, dan mengevaluasi model deep learning untuk klasifikasi gambar.

---

## 📁 Struktur Folder

* `Pertemuan8/`
  * `main.ipynb` (Notebook Eksperimen, Training & Evaluasi)
  * `main.py` (Skrip Python Utama)
  * `README.md` (Dokumentasi Teknis)
  * `rockpaperscissors/`
    * `paper/` (Dataset gambar kertas)
    * `rock/` (Dataset gambar batu)
    * `scissors/` (Dataset gambar gunting)

---

## 🛠️ Studi Kasus: Klasifikasi Gambar Rock Paper Scissors

Proyek mini ini menerapkan Computer Vision untuk mengenali dan membedakan 3 bentuk isyarat tangan (*Rock*, *Paper*, dan *Scissors*) dari berkas gambar yang diunduh melalui Kaggle Dataset.

### ⚙️ Mekanisme Kerja & Pipeline Praktikum

Program ini memproses data gambar lewat tahapan terstruktur sebagai berikut:

1. **Data Preparation:** Memuat dataset menggunakan pustaka `ImageDataGenerator` untuk melakukan proses *rescaling* piksel otomatis.
2. **Data Splitting:** Memisahkan data secara acak menjadi proporsi komponen 80% untuk data latih (*training*) dan 20% untuk data validasi (*validation*).
3. **Model Compilation:** Menggunakan *loss function* **Categorical Crossentropy** untuk multi-kelas dan penyesuaian bobot lewat optimizer **Adam**.
4. **Training & Metrics:** Proses pelatihan dilangsungkan sepanjang 10 epoch lengkap disertai pelacakan performa akurasi dan *loss error* lewat grafik visualisasi `matplotlib`.

---

## 📐 Arsitektur Model CNN

Model dirancang menggunakan kombinasi layer konvolusi untuk menangkap fitur visual dan layer padat untuk klasifikasi akhir:

| Lapisan (Layer) | Tipe Layer | Konfigurasi Parameter / Aktivasi |
| :--- | :--- | :--- |
| **Layer 1** | Conv2D | 32 filters, kernel (3,3), Aktivasi **ReLU** |
| **Layer 2** | MaxPooling2D | pool size (2,2) |
| **Layer 3** | Conv2D | 64 filters, kernel (3,3), Aktivasi **ReLU** |
| **Layer 4** | MaxPooling2D | pool size (2,2) |
| **Layer 5** | Conv2D | 128 filters, kernel (3,3), Aktivasi **ReLU** |
| **Layer 6** | MaxPooling2D | pool size (2,2) |
| **Layer 7** | Flatten | Perataan matriks fitur menjadi vektor 1D |
| **Layer 8** | Dense | 512 units, Aktivasi **ReLU** |
| **Layer 9 (Output)** | Dense | 3 units (Kelas), Aktivasi **Softmax** |

---

## 🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat (Prerequisites)

Pastikan pustaka deep learning dan data science berikut telah terpasang:

* Python 3.x
* Framework: `tensorflow` (Keras)
* Tools Data: `numpy`, `pandas`
* Visualisasi: `matplotlib`

### 2. Langkah Menjalankan Program

1. Unduh dataset *Rock Paper Scissors* melalui tautan Kaggle resmi, lalu ekstrak ke dalam direktori proyek hingga sesuai dengan bagan struktur folder di atas.
2. Buka terminal atau CMD, lalu arahkan menuju direktori kerja:
   ```bash
   cd Pertemuan8
   ```
3. Jalankan program menggunakan salah satu cara berikut:

   **Menggunakan Jupyter Notebook / Google Colab:**
   - Buka `main.ipynb`
   - Jalankan semua cell secara berurutan (**Run All** / **Restart & Run All**)

   **Menggunakan Python Script:**
   ```bash
   python main.py
   ```
