# 🧬 Pertemuan 9 - Algoritma Genetika 1

---

### 📝 Deskripsi Tugas
Program ini berisi implementasi dasar **Algoritma Genetika (Genetic Algorithm)** untuk memecahkan permasalahan optimasi **Knapsack Problem**. Program dirancang untuk memilih kombinasi dari 9 jenis barang agar mendapatkan keuntungan atau profit maksimal tanpa melebihi batas kapasitas beban tas sebesar 50 kg.

---

### 🛠️ Penggunaan Metode Komputasi
Berbeda dengan Pertemuan 10 yang bersifat dinamis mengikuti NIM, parameter dan metode pada modul pengerjaan acuan Pertemuan 9 bersifat seragam untuk seluruh mahasiswa dengan rincian sebagai berikut:

* **Seleksi:** Menggunakan **Roulette Wheel Selection (RWS)**.
* **Crossover:** Menggunakan **One-Point Crossover**.
* **Mutasi:** Menggunakan **Swap Mutation**.

---

### 📂 Struktur Folder Proyek
```text
H1D024078-PraktikumKB-Pertemuan9/
├── crossover.py
├── evaluasifitness.py
├── inisiasipopulasi.py
├── main.py
├── mutation.py
├── README.md
└── selection.py
```

---

### 📂 File Program
Proyek ini terdiri dari beberapa components file Python yang saling terintegrasi:
* **`inisiasipopulasi.py`** : Membangkitkan populasi awal berisi kromosom biner acak.
* **`evaluasifitness.py`** : Menghitung nilai harga total (fitness) dan menerapkan fungsi pinalti 0 jika berat melebihi batas.
* **`selection.py`** : Berisi implementasi fungsi seleksi Roulette Wheel Selection.
* **`crossover.py`** : Berisi fungsi perkawinan silang menggunakan metode One-Point Crossover.
* **`mutation.py`** : Berisi fungsi mutasi posisi gen dengan metode Swap Mutation.
* **`main.py`** : Program utama (driver) untuk menjalankan loop generasi dan visualisasi data.

---

### 📊 Hasil Percobaan & Analisis Grafik
Setelah dijalankan hingga 50 Generasi dengan 20 Populasi, algoritma berhasil memetakan tren konvergensi nilai fitness sebagai berikut:
* **Fitness Tertinggi (Garis Biru)** : Grafik bergerak naik secara berkala hingga mencapai kestabilan solusi optimal maksimal tas mendekati atau tepat pada kapasitas limit.
* **Fitness Rata-rata (Garis Merah)** : Menunjukkan fluktuasi naik-turn yang dinamis, mengindikasikan eksplorasi ruang solusi baru tetap berjalan lancar untuk mencegah konvergensi prematur.
* **Fitness Terendah (Garis Kuning)** : Nilai pinalti 0 muncul sebagai batasan ketat bagi setiap solusi acak yang melanggar batas kapasitas beban tas.

---

**Output Terminal Akhir:**
```text
=== HASIL OPTIMASI TAS (PERT9) ===
Nilai Fitness Terbaik: 329
Total Bobot Terpilih : 50 / 50
Barang Terpilih:
- Barang2
- Barang5
- Barang6
- Barang8
```
