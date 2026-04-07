📂 Pertemuan 2: Sistem Pakar Logika Fuzzy (Kipas Otomatis)
Pada pertemuan ini, dilakukan implementasi Logika Fuzzy metode Mamdani untuk mengatur kecepatan kipas angin secara cerdas berdasarkan kondisi lingkungan (suhu dan kelembapan).

📝 Deskripsi Proyek
Program tugas.py mensimulasikan sistem kendali kipas yang dapat menentukan kecepatan putaran motor (0-100%) agar tercipta kenyamanan termal yang optimal secara otomatis.

📂 Struktur Folder
Pertemuan2/
├── tugas.py           # Program utama logika fuzzy
└── README.md          # Dokumentasi tugas pertemuan 2

🛠️ Komponen Fuzzy
Sistem ini menggunakan pustaka scikit-fuzzy dengan rincian variabel sebagai berikut:
1. Variabel Input (Antecedent)
- Suhu (0 - 40°C): Memiliki himpunan dingin, normal, dan panas.
- Kelembapan (0 - 100%): Memiliki himpunan kering, ideal, dan basah.
2. Variabel Output (Consequent)
- Kecepatan Kipas (0 - 100%): Memiliki himpunan lambat, sedang, dan cepat.

🧠 Basis Aturan (Rule Base)
Program menjalankan 3 aturan logika utama:
1. IF Suhu Dingin AND Kelembapan Basah THEN Kipas Lambat.
2. IF Suhu Normal AND Kelembapan Ideal THEN Kipas Sedang.
3. IF Suhu Panas OR Kelembapan Kering THEN Kipas Cepat.

🚀 Cara Menjalankan
1. Pastikan sudah menginstal dependensi:
pip install numpy skfuzzy matplotlib
2. Jalankan program:
python Pertemuan2/tugas.py

📥 Contoh Input & Output (Testing)
- Contoh Input: Suhu 22°C dan Kelembapan 65%.
- Hasil Output: Sistem akan menghitung nilai numerik kecepatan kipas menggunakan metode defuzzifikasi centroid dan menampilkan grafik keanggotaan.