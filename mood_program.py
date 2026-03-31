import random
import time

# Struktur Data (Dictionary + List)
mood_aktivitas = {
    "senang": ["Jalan-jalan", "Nonton film", "Main game"],
    "sedih": ["Dengar musik", "Tidur", "Curhat ke teman"],
    "bosan": ["Olahraga", "Belajar hal baru", "Baca buku"],
    "marah": ["Tarik napas dalam", "Dengar musik santai", "Istirahat"]
}

# Struktur Kontrol
while True:
    print("\n=== SIMULATOR MOOD HARIAN ===")
    print("1. Pilih Mood")
    print("2. Lihat Semua Mood")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        mood = input("Masukkan mood kamu: ").lower()

        if mood in mood_aktivitas:
            print("Mencari aktivitas yang cocok...")
            time.sleep(1)  # Library time
            aktivitas = random.choice(mood_aktivitas[mood])  # Library random
            print(f"Saran aktivitas: {aktivitas}")
        else:
            print("Mood tidak ditemukan.")

    elif pilihan == "2":
        print("\nDaftar Mood:")
        for m in mood_aktivitas:
            print("-", m)

    elif pilihan == "3":
        print("Semoga harimu menyenangkan!")
        break

    else:
        print("Pilihan tidak valid!")