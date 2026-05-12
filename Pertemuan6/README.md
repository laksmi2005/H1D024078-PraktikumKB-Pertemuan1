# 🧠 Pertemuan 6 - Jaringan Syaraf Tiruan (JST)

Repositori ini berisi hasil pengerjaan modul Praktikum Kecerdasan Buatan (KB) Pertemuan 6 yang berfokus pada implementasi **Jaringan Syaraf Tiruan (JST)**. Praktikum ini mencakup dua metode pembelajaran utama, yaitu **Perceptron** untuk masalah linier dan **Backpropagation** untuk masalah non-linier.

---

## 📂 Struktur Folder

* `Pertemuan6/`
    * `perceptron.py` (Source code class Perceptron)
    * `backpropagation.py` (Source code class Backpropagation)
    * `README.md` (Dokumentasi Teknis)

---

## 🛠️ Studi Kasus: Implementasi JST

Aplikasi ini menggunakan dua metode utama untuk menyelesaikan permasalahan logika dasar:
1.  **Metode Perceptron**: Digunakan untuk menyelesaikan masalah logika **OR** yang bersifat *linearly separable*.
2.  **Metode Backpropagation**: Digunakan untuk menyelesaikan masalah logika **XOR** menggunakan *hidden layer* agar dapat menangani pemisahan data non-linier.

---

## 📈 Hasil Praktikum

Program ini bekerja dengan mengoptimasi bobot dan bias:

1.  **Perceptron (OR Gate)**: Model berhasil melakukan klasifikasi dengan benar. Garis pemisah (*decision boundary*) terbentuk untuk memisahkan data input sesuai dengan target.
2.  **Backpropagation (XOR Gate)**: Model berhasil mencapai target error (0.001). Grafik menunjukkan penurunan **SSE** yang signifikan seiring bertambahnya epoch.

---

## 🚀 Panduan Instalasi & Penggunaan

### 1. Prasyarat
* Python 3.x terinstal.
* Library `numpy` dan `matplotlib`.

### 2. Cara Menjalankan
1.  Clone atau download repositori ini.
2.  Buka terminal/CMD di folder tersebut.
3.  Jalankan perintah:
    ```bash
    python Pertemuan6/perceptron_or.py
    python Pertemuan6/backpropagation_xor.py
    ```
