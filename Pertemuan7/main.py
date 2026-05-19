
# Langkah 1: Import library
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Langkah 2: Muat dataset iris dari file lokal
dataset = pd.read_csv('iris.data', header=None, sep=',')

X = dataset.iloc[:, :-1].values  # 4 kolom pertama sebagai fitur
y = dataset.iloc[:, -1].values   # Kolom terakhir sebagai label

print("Shape X:", X.shape)
print("Shape y:", y.shape)
print("\nContoh data:")
print(dataset.head())

# Langkah 3: Konversi label string ke numerik
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

print("\nKelas:", label_encoder.classes_)
print("Label setelah encoding:", np.unique(y))

# Langkah 4: Split data latih dan validasi (80:20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nUkuran data latih:", X_train.shape)
print("Ukuran data validasi:", X_test.shape)

# Langkah 5: Buat model neural network
model = Sequential([
    Input(shape=(4,)),
    Dense(1000, activation='relu'),
    Dense(500, activation='relu'),
    Dense(300, activation='relu'),
    Dense(3, activation='softmax')
])

model.summary()

# Langkah 6: Kompilasi model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Langkah 7: Latih model
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# Langkah 8: Evaluasi model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nLoss: {loss}, Accuracy: {accuracy}")

# Langkah 9: Visualisasi training history
pd.DataFrame(history.history).plot(figsize=(10, 6))
plt.title('Training History')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.grid(True)
plt.legend(loc='best')
plt.show()

# Langkah 10: Prediksi pada data validasi
predictions = model.predict(X_test)
predicted_classes = predictions.argmax(axis=1)

print("\nPrediksi:", predicted_classes)
print("Label Asli:", y_test)

# Langkah 11: Confusion Matrix
cm = confusion_matrix(y_test, predicted_classes)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=label_encoder.classes_,
            yticklabels=label_encoder.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Langkah 12: Prediksi data baru
def predict_new_data():
    sepal_length = float(input("Masukkan sepal length: "))
    sepal_width  = float(input("Masukkan sepal width: "))
    petal_length = float(input("Masukkan petal length: "))
    petal_width  = float(input("Masukkan petal width: "))

    new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(new_data)
    predicted_class = prediction.argmax(axis=1)
    predicted_label = label_encoder.inverse_transform(predicted_class)

    print(f"Prediksi kelas: {predicted_label[0]}")

predict_new_data()