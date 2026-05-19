# Praktikum 8 - Jaringan Syaraf Tiruan 3
## Convolutional Neural Network (CNN)

### Tujuan
- Memahami konsep dan cara kerja Convolutional Neural Network (CNN)
- Mampu membangun, melatih, dan mengevaluasi model CNN untuk klasifikasi gambar

### Dataset
Dataset **Rock Paper Scissors** dari Kaggle:
https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors/download

### Struktur Folder
```
NIM-PraktikumKB-Pertemuan8/
├── main.ipynb
├── main.py
├── README.md
└── rockpaperscissors/
    ├── paper/
    │   ├── image 1.png
    │   └── ...
    ├── rock/
    │   ├── image 1.png
    │   └── ...
    └── scissors/
        ├── image 1.png
        └── ...
```

### Cara Menjalankan

#### Menggunakan Jupyter Notebook / Google Colab
1. Download dataset dari link di atas dan ekstrak sehingga struktur folder sesuai di atas
2. Buka `main.ipynb`
3. Jalankan semua cell secara berurutan (**Run All** / **Restart & Run All**)

#### Menggunakan Python Script
1. Download dataset dari link di atas dan ekstrak sehingga struktur folder sesuai di atas
2. Jalankan dari terminal:
```bash
python main.py
```

### Langkah-langkah Praktikum

| Langkah | Deskripsi |
|---------|-----------|
| 3 | Import library (TensorFlow, Keras, NumPy, Pandas, Matplotlib) |
| 4 | Persiapan data dengan ImageDataGenerator (rescale + validation split 80/20) |
| 5 | Membangun arsitektur model CNN |
| 6 | Kompilasi model (loss: categorical_crossentropy, optimizer: adam) |
| 7 | Pelatihan model selama 10 epoch |
| 8 | Evaluasi model pada data validasi |
| 9 | Prediksi pada data validasi |
| - | Visualisasi grafik akurasi dan loss training |

### Arsitektur Model CNN

| Layer | Tipe | Parameter |
|-------|------|-----------|
| 1 | Conv2D | 32 filters, kernel (3,3), aktivasi ReLU |
| 2 | MaxPooling2D | pool (2,2) |
| 3 | Conv2D | 64 filters, kernel (3,3), aktivasi ReLU |
| 4 | MaxPooling2D | pool (2,2) |
| 5 | Conv2D | 128 filters, kernel (3,3), aktivasi ReLU |
| 6 | MaxPooling2D | pool (2,2) |
| 7 | Flatten | - |
| 8 | Dense | 512 units, aktivasi ReLU |
| 9 | Dense (Output) | 3 units, aktivasi Softmax |

### Library yang Digunakan
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
