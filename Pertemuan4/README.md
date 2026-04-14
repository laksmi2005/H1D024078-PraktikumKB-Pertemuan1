# 💻 Pertemuan 4: Sistem Pakar Diagnosa Kerusakan Laptop

Repositori ini berisi implementasi **Sistem Pakar (Expert System)** berbasis **GUI (Graphical User Interface)** menggunakan Python. Proyek ini dirancang untuk memenuhi kriteria tugas praktikum dalam mengidentifikasi kerusakan perangkat keras dan sistem pada laptop berdasarkan gejala yang dimasukkan pengguna.

## 🗂️ Struktur Folder
* `Pertemuan4/`
  * ├── `percobaan_1.py` (Logika Silsilah Keluarga)
  * ├── `percobaan_2.py` (Diagnosa Malaria - Set Logic)
  * ├── `percobaan_3.py` (Diagnosa Malaria - Interactive Console)
  * ├── `percobaan_4.py` (Diagnosa Malaria - GUI Dasar)
  * ├── `laptop_rusak.py` (Tugas Utama: Sistem Pakar Diagnosa Laptop)
  * └── `README.md` (Dokumentasi teknis)

---

## 🛠️ Studi Kasus: Laptop Clinic Expert System

Aplikasi ini bertindak sebagai asisten teknisi digital yang mendiagnosa masalah laptop menggunakan metode **Forward Chaining**. Sistem ini dirancang secara modular agar mudah dikembangkan di masa depan.

### 📊 Knowledge Base (Basis Pengetahuan)
Sistem ini menyimpan aturan kerusakan dalam struktur data **Dictionary**, di mana setiap entitas memiliki daftar gejala dan solusi spesifik.

| Jenis Kerusakan | Gejala Utama | Solusi Spesifik |
| :--- | :--- | :--- |
| **LCD/Layar** | Garis warna, Flicker, Berbayang | Cek kabel fleksibel atau ganti panel LCD. |
| **Keyboard** | Ghosting, Tombol mati, Beeping | Bersihkan sela tombol atau ganti modul. |
| **Baterai** | Drop drastis, Harus dicas, Mati mendadak | Kalibrasi baterai atau ganti unit original. |
| **Overheat** | Fan bising, Panas menyengat, Restart | Bersihkan fan dan ganti thermal paste. |
| **Storage (SSD/HDD)** | Booting lama, BSOD, Disk Error | Backup data, defrag, atau migrasi ke SSD. |

### 🧠 Mesin Inferensi
Sistem ini tidak menggunakan deretan `if-else` yang panjang (hardcoded), melainkan menggunakan mekanisme iterasi dinamis pada dictionary:
1. **Fact Gathering**: Mengumpulkan input `YA/TIDAK` dari user melalui GUI.
2. **Pattern Matching**: Menggunakan fungsi `all()` untuk memastikan semua gejala syarat terpenuhi sebelum menarik kesimpulan.
3. **Handling Unknown**: Jika fakta yang dimasukkan tidak memenuhi syarat kerusakan manapun, sistem akan memberikan notifikasi bahwa perangkat dalam kondisi sehat.

---

## 🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat Sistem
* Python 3.x
* Pustaka `tkinter` (Bawaan Python)

### 2. Cara Menjalankan
Pastikan Anda berada di direktori proyek, lalu jalankan perintah:
```bash
python Pertemuan4/laptop_expert.py