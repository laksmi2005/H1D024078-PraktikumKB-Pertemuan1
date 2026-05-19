"""
Praktikum 8 - Jaringan Syaraf Tiruan 3
Convolutional Neural Network (CNN) untuk Klasifikasi Gambar
Dataset: Rock Paper Scissors
"""

# ============================================================
# Langkah 3: Import Library
# ============================================================
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

print('TensorFlow version:', tf.__version__)


# ============================================================
# Langkah 4: Persiapan Data menggunakan ImageDataGenerator
# ============================================================
dataset_path = "./rockpaperscissors"

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='training',
)

validation_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='validation',
)

print('Kelas yang terdeteksi:', train_generator.class_indices)
print(f'Jumlah data training  : {train_generator.samples}')
print(f'Jumlah data validasi  : {validation_generator.samples}')


# ============================================================
# Langkah 5: Membangun Arsitektur Model CNN
# ============================================================
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax')
])

model.summary()


# ============================================================
# Langkah 6: Kompilasi Model
# ============================================================
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

print('Model berhasil dikompilasi!')


# ============================================================
# Langkah 7: Pelatihan Model (Model Fitting)
# ============================================================
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)


# ============================================================
# Langkah 8: Evaluasi Model
# ============================================================
val_loss, val_acc = model.evaluate(validation_generator)
print(f'Validation loss: {val_loss}, Validation accuracy: {val_acc}')


# ============================================================
# Langkah 9: Prediksi pada Data Validasi
# ============================================================
predictions = model.predict(validation_generator)
print(predictions)  # Output berupa probabilitas prediksi tiap kelas


# ============================================================
# Visualisasi Akurasi dan Loss Training
# ============================================================
plt.figure(figsize=(12, 4))

# Plot Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Plot Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()
print('Plot disimpan sebagai training_history.png')
