# Sistem Asesmen Psikologis Kecemasan (Sistem Pakar)

Aplikasi web untuk mendiagnosis gangguan kecemasan psikologis menggunakan metode **Sistem Pakar (Certainty Factor)**.

## 🔗 Demo
👉 [https://sistempakar-eosin.vercel.app](https://sistempakar-eosin.vercel.app)

## 📋 Deskripsi
Sistem ini menyajikan 10 pertanyaan psikologis secara interaktif (satu per satu), lalu menghitung tingkat keyakinan (confidence) adanya gangguan kecemasan berdasarkan jawaban pengguna menggunakan metode Certainty Factor.

## 🧠 Pertanyaan Kuesioner
Kuesioner mencakup gejala psikologis seperti:
- Kekhawatiran berlebihan terhadap hal yang belum terjadi
- Perasaan gelisah atau kesulitan rileks
- Kelelahan mental
- Kesulitan berkonsentrasi
- Mudah marah / tersinggung
- Serangan panik mendadak
- Ketakutan kehilangan kendali
- Perasaan bahaya mengancam di lingkungan aman
- Penghindaran situasi sosial
- Ketakutan dihakimi di depan umum

## ⚙️ Metode: Certainty Factor (CF)
- **Input**: 4 pilihan jawaban: `Tidak Pernah (0)`, `Jarang (0.3)`, `Sering (0.7)`, `Selalu (1.0)`
- **Perhitungan**: Kombinasi CF antar gejala menggunakan formula kombinasi serial
- **Output**: Persentase keyakinan (confidence) per jenis gangguan

## 📊 Gangguan yang Didiagnosis
| Gangguan | Kode |
|---|---|
| Generalized Anxiety Disorder (GAD) | G1 |
| Panic Disorder | G2 |
| Social Anxiety Disorder | G3 |

## 🎯 Skala Keyakinan
| Confidence | Indikasi |
|---|---|
| < 40% | Rendah |
| 40% - 69% | Sedang |
| ≥ 70% | Tinggi |

## 🛠️ Teknologi
- **Backend**: Python, Flask
- **Frontend**: HTML, Tailwind CSS, Lucide Icons
- **Hosting**: Vercel

## 🚀 Cara Menjalankan Lokal
```bash
cd sistem_pakar
pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5001`
