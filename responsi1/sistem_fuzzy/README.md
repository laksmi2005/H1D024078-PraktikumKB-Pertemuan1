# Sistem Deteksi Gejala Fisik Kecemasan (Fuzzy Logic)

Aplikasi web untuk mendeteksi tingkat kecemasan berdasarkan **gejala fisik** menggunakan metode **Fuzzy Logic (Sugeno)**.

## 🔗 Demo
👉 [https://sistemfuzzy.vercel.app](https://sistemfuzzy.vercel.app)

## 📋 Deskripsi
Sistem ini meminta pengguna untuk memasukkan intensitas 4 gejala fisik yang umum berkaitan dengan kecemasan, kemudian menghitung skor kecemasan fisik menggunakan logika fuzzy.

## 🧠 Gejala yang Dievaluasi
| Gejala | Deskripsi |
|---|---|
| Palpitasi | Intensitas jantung berdebar tanpa penyebab fisik |
| Insomnia | Kesulitan memulai atau mempertahankan tidur |
| Ketegangan Otot | Frekuensi otot terasa kaku (leher, bahu, rahang) |
| Gangguan Pencernaan | Tingkat mual/sakit perut saat cemas |

## ⚙️ Metode: Fuzzy Logic (Sugeno)
- **Fuzzifikasi**: Nilai input (0-100) dipetakan ke fungsi keanggotaan segitiga: `rendah`, `sedang`, `tinggi`
- **Inferensi**: 7 aturan fuzzy dikombinasikan menggunakan operator AND/OR
- **Defuzzifikasi**: Weighted Average menghasilkan skor akhir (0-100)

## 📊 Klasifikasi Hasil
| Skor | Status |
|---|---|
| 0 - 29 | ✅ Normal / Aman |
| 30 - 69 | ⚠️ Waspada (Gejala Sedang) |
| 70 - 100 | 🚨 Kritis (Gejala Parah) |

## 🛠️ Teknologi
- **Backend**: Python, Flask
- **Logika**: Pure Python (tanpa library eksternal)
- **Frontend**: HTML, Tailwind CSS, Lucide Icons
- **Hosting**: Vercel

## 🚀 Cara Menjalankan Lokal
```bash
cd sistem_fuzzy
pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5000`
