# 🧬 Pertemuan 10 - Algoritma Genetika 2

---

### 📝 Deskripsi Tugas
Program ini menerapkan **Algoritma Genetika (Genetic Algorithm)** untuk memecahkan permasalahan **Knapsack Problem** pada studi kasus **Optimasi Gudang Toko**. Program mencari kombinasi barang yang memberikan keuntungan maksimal tanpa melebihi ukuran kapasitas gudang yang ditentukan.

---

### 🛠️ Penentuan Metode Berdasarkan Akhiran NIM (78)
Berdasarkan aturan modul praktikum pertemuan 10, kombinasi metode yang wajib digunakan sesuai digit NIM adalah sebagai berikut:

* **Seleksi (Digit 1 dari belakang = 7):** Menggunakan **Tournament Selection (TS)**.
* **Crossover (Digit 2 dari belakang = 8):** Menggunakan **Uniform Crossover**.
* **Mutasi (Penjumlahan digit 7 + 8 = 15 -> Digit terakhir = 5):** Menggunakan **Uniform Mutation**.

---

### 📂 Struktur Folder Proyek
```text
H1D024078-PraktikumKB-Pertemuan10/
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
Proyek ini terdiri dari beberapa komponen file Python yang saling terintegrasi:
* **`inisiasipopulasi.py`** : Membangkitkan populasi awal berisi kromosom biner acak.
* **`evaluasifitness.py`** : Menghitung nilai keuntungan dan menerapkan fungsi pinalti 0 jika ukuran melebihi batas.
* **`selection.py`** : Berisi implementasi fungsi *Tournament Selection*.
* **`crossover.py`** : Berisi fungsi perkawinan silang menggunakan metode *Uniform Crossover*.
* **`mutation.py`** : Berisi fungsi mutasi gen biner dengan metode *Uniform Mutation*.
* **`main.py`** : Program utama (*driver*) untuk menjalankan loop generasi dan visualisasi data.

---

### 📊 Hasil Percobaan & Analisis Grafik
Setelah dijalankan hingga **50 Generasi** dengan **20 Populasi**, program menampilkan sebaran titik populasi (abu-abu) dan tren nilai fitness sebagai berikut:
* **Fitness Tertinggi (Garis Biru):** Mencapai nilai keuntungan konstan **125** sejak generasi awal.
* **Fitness Rata-rata (Garis Merah):** Bergerak fluktuatif dinamis mencerminkan variasi genetik yang terjaga baik dari efek *uniform crossover* & *mutation*.
* **Fitness Terendah (Garis Kuning):** Berada stabil di nilai **0** akibat penalti terhadap individu kromosom yang melebihi kapasitas gudang.

---

**Output Terminal Akhir:**
```text
=== HASIL OPTIMASI GUDANG ===
Nilai Keuntungan Terbaik : 125
Total Ukuran Dipakai     : 14 / 15
Barang Terpilih:
- Barang2
- Barang4
- Barang5
```
