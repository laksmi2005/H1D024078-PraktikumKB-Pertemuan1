📂 Pertemuan 3: Implementasi Multi-Studi Kasus Logika Fuzzy

Repositori ini berisi dua implementasi sistem pakar menggunakan Logika Fuzzy (Mamdani) untuk menyelesaikan permasalahan optimasi stok dan evaluasi pelayanan publik.



📂 Struktur Folder

Pertemuan3/

├── petshop.py         # Studi Kasus 1: Optimasi Stok Makanan

├── pelayanan.py       # Studi Kasus 2: Evaluasi Kepuasan Pelayanan

└── README.md          # Dokumentasi teknis Pertemuan 3



🐕 Studi Kasus 1: Petshop (Optimasi Stok)

Program ini menentukan jumlah stok makanan hewan yang harus disediakan berdasarkan perputaran barang dan keuntungan.



📊 Variabel \& Input

|Variabel Input|Range|Label Himpunan|
|-|-|-|
|Barang Terjual|0 - 100|Rendah, Sedang, Tinggi|
|Permintaan|0 - 300|Rendah, Sedang, Tinggi|
|Harga Item|0 - 100rb|Murah, Sedang, Mahal|
|Profit|0 - 4jt|Rendah, Sedang, Banyak|



Output: stok\_makanan (100 - 1000 unit).



🏛️ Studi Kasus 2: Pelayanan (Kepuasan Publik)

Sistem ini mengevaluasi tingkat kepuasan masyarakat terhadap layanan publik berdasarkan 81 aturan kombinasi.



📊 Variabel \& Input

|Variabel Input|Range|Label Himpunan|
|-|-|-|
|Kejelasan Informasi|0 - 100|Tidak Memuaskan, Cukup, Memuaskan|
|Kejelasan Syarat|0 - 100|Tidak Memuaskan, Cukup, Memuaskan|
|Kemampuan Petugas|0 - 100|Tidak Memuaskan, Cukup, Memuaskan|
|Ketersediaan Sarpras|0 - 100|Tidak Memuaskan, Cukup, Memuaskan|



Output: kepuasan\_pelayanan (0 - 400 poin).



🚀 Cara Menjalankan

1. Pastikan pustaka yang dibutuhkan sudah terinstal:

pip install numpy skfuzzy matplotlib

2\. Jalankan program yang diinginkan:

\# Untuk Studi Kasus 1

python Pertemuan3/petshop.py

\# Untuk Studi Kasus 2

python Pertemuan3/pelayanan.py



📥 Contoh Hasil Testing

* Petshop: Dengan input terjual 80 dan profit 3.5jt, sistem merekomendasikan stok makanan sebanyak \~900 unit.
* Pelayanan: Dengan rata-rata input nilai 80-90, sistem menghasilkan status kepuasan Sangat Memuaskan.

