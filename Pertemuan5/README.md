# 👂 Pertemuan 5: Sistem Pakar Diagnosa Penyakit THT (GUI)

Repositori ini berisi implementasi **Sistem Pakar (Expert System)** berbasis **GUI (Graphical User Interface)** menggunakan Python untuk mendiagnosa berbagai penyakit Telinga, Hidung, dan Tenggorokan (THT) sesuai dengan data pada Modul Praktikum 5.

## 🗂️ Struktur Folder
* `Pertemuan5/`
  * ├── `diagnosa_tht.py` (Aplikasi Utama GUI)
  * └── `README.md` (Dokumentasi Teknis)

---

## 🛠️ Studi Kasus: Diagnosa Penyakit THT
Aplikasi ini menggunakan metode **Forward Chaining** untuk mencocokkan gejala yang dialami pengguna dengan basis pengetahuan yang bersumber dari pakar THT.

### 📊 Basis Pengetahuan (Knowledge Base)
Sistem ini memproses **37 jenis gejala (G1-G37)** untuk mendeteksi **23 jenis penyakit THT**. Data aturan disimpan dalam struktur **Dictionary** untuk efisiensi pemrosesan.

#### Sampel Pemetaan Gejala & Penyakit:
| Jenis Penyakit | Kode Gejala | Solusi Singkat |
| :--- | :--- | :--- |
| **Tonsilitis** | G37, G12, G5, G27, G6, G21 | Istirahat, kumur air garam, minum cairan hangat. |
| **Sinusitis Maksilaris** | G37, G12, G27, G17, G33, G36, G29 | Irigasi hidung saline dan gunakan dekongestan. |
| **Meniere** | G20, G35, G14, G4 | Diet rendah garam dan hindari pemicu vertigo. |
| **Laringitis** | G37, G5, G15, G16, G32 | Istirahatkan suara dan konsumsi banyak air. |

### 🧠 Mekanisme Inferensi
Program ini bekerja dengan logika ketat:
1. **Fact Gathering**: Pengguna menjawab pertanyaan gejala satu per satu melalui antarmuka tombol GUI.
2. **Pattern Matching**: Menggunakan fungsi logika `all()` untuk memastikan *seluruh* syarat gejala suatu penyakit terpenuhi sebelum memberikan diagnosa.
3. **Handling Result**: Jika tidak ada pola gejala yang cocok 100%, sistem akan menginformasikan bahwa tidak ada penyakit yang terdeteksi.

---

## 🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat
* Python 3.x terinstal.
* Library `tkinter` (bawaan Python standar).

### 2. Cara Menjalankan
1. Clone atau download repositori ini.
2. Buka terminal/CMD di folder tersebut.
3. Jalankan perintah:
   ```bash
   python Pertemuan5/diagnosa_tht.py
   ```