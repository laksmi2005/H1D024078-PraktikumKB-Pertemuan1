import tkinter as tk
from tkinter import messagebox

# 1. KNOWLEDGE BASE (Minimal 5 Kerusakan dengan Dictionary)
# Struktur: "Nama Kerusakan": {"gejala": [list_gejala], "solusi": "teks_solusi"}
database_pakar = {
    "Kerusakan LCD/Layar": {
        "gejala": ["garis_dilayar", "layar_berkedip", "tampilan_berbayang"],
        "solusi": "Cek kabel fleksibel layar atau ganti panel LCD jika pecah fisik."
    },
    "Keyboard Malfungsi": {
        "gejala": ["tombol_ngetik_sendiri", "beberapa_tombol_mati", "bunyi_beeping_saat_nyala"],
        "solusi": "Bersihkan sela-sela tombol dengan kuas atau ganti modul keyboard."
    },
    "Baterai Bocor/Drop": {
        "gejala": ["cepat_habis", "harus_dicas_terus", "laptop_mati_mendadak"],
        "solusi": "Kalibrasi baterai atau ganti dengan baterai original baru."
    },
    "Overheat (Panas Berlebih)": {
        "gejala": ["fan_berisik", "bawah_laptop_panas", "sering_restart_sendiri"],
        "solusi": "Bersihkan debu pada kipas dan ganti thermal paste pada prosesor."
    },
    "Hardisk/SSD Corrupt": {
        "gejala": ["loading_sangat_lama", "sering_blue_screen", "muncul_pesan_disk_error"],
        "solusi": "Lakukan defrag (HDD) atau segera backup data dan ganti ke SSD baru."
    }
}

# DAFTAR PERTANYAAN
daftar_gejala = [
    ("garis_dilayar", "Apakah muncul garis-garis berwarna pada layar?"),
    ("layar_berkedip", "Apakah tampilan layar sering berkedip (flicker)?"),
    ("tampilan_berbayang", "Apakah tampilan layar terlihat buram atau berbayang?"),
    ("tombol_ngetik_sendiri", "Apakah ada tombol yang seolah-olah tertekan sendiri?"),
    ("beberapa_tombol_mati", "Apakah ada beberapa tombol yang tidak berfungsi saat ditekan?"),
    ("bunyi_beeping_saat_nyala", "Apakah ada bunyi 'beep' panjang saat laptop baru dinyalakan?"),
    ("cepat_habis", "Apakah persentase baterai berkurang sangat cepat (drastis)?"),
    ("harus_dicas_terus", "Apakah laptop langsung mati jika kabel charger dilepas?"),
    ("laptop_mati_mendadak", "Apakah laptop sering mati tiba-tiba padahal baterai masih ada?"),
    ("fan_berisik", "Apakah suara kipas terdengar sangat bising/keras?"),
    ("bawah_laptop_panas", "Apakah bagian bawah laptop terasa panas menyengat saat disentuh?"),
    ("sering_restart_sendiri", "Apakah laptop sering restart sendiri saat membuka aplikasi berat?"),
    ("loading_sangat_lama", "Apakah proses booting atau buka folder sangat lambat?"),
    ("sering_blue_screen", "Apakah sering muncul layar biru (Blue Screen of Death)?"),
    ("muncul_pesan_disk_error", "Apakah muncul pesan 'No Bootable Device' atau 'Disk Error'?")
]

class LaptopExpert:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Clinic Expert System")
        self.root.geometry("500x350")
        self.root.configure(bg="#f4f7f6")
        
        self.gejala_terpilih = []
        self.index = 0

        self.lbl_judul = tk.Label(root, text="Sistem Pakar Diagnosa Laptop", font=("Arial", 14, "bold"), bg="#f4f7f6")
        self.lbl_judul.pack(pady=20)

        self.lbl_tanya = tk.Label(root, text="Klik tombol di bawah untuk mulai diagnosa", wraplength=400, font=("Arial", 11), bg="#f4f7f6")
        self.lbl_tanya.pack(pady=30)

        self.btn_start = tk.Button(root, text="Mulai Diagnosa", command=self.mulai, bg="#3498db", fg="white", width=20)
        self.btn_start.pack()

        self.frame_aksi = tk.Frame(root, bg="#f4f7f6")
        self.btn_ya = tk.Button(self.frame_aksi, text="YA", width=12, bg="#2ecc71", fg="white", command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_aksi, text="TIDAK", width=12, bg="#e74c3c", fg="white", command=lambda: self.jawab('t'))

    def mulai(self):
        self.gejala_terpilih = []
        self.index = 0
        self.btn_start.pack_forget()
        self.frame_aksi.pack(pady=20)
        self.btn_ya.pack(side=tk.LEFT, padx=15)
        self.btn_tidak.pack(side=tk.LEFT, padx=15)
        self.update_pertanyaan()

    def update_pertanyaan(self):
        if self.index < len(daftar_gejala):
            self.lbl_tanya.config(text=daftar_gejala[self.index][1])
        else:
            self.tampilkan_hasil()

    def jawab(self, pilihan):
        if pilihan == 'y':
            self.gejala_terpilih.append(daftar_gejala[self.index][0])
        self.index += 1
        self.update_pertanyaan()

    def tampilkan_hasil(self):
        hasil_teks = ""
        terdeteksi = False
        
        # 2. MESIN INFERENSI (Iterasi Dictionary)
        for nama, data in database_pakar.items():
            syarat = data["gejala"]
            solusi = data["solusi"]
            
            if all(s in self.gejala_terpilih for s in syarat):
                hasil_teks += f"⚠️ {nama}\nSolusi: {solusi}\n\n"
                terdeteksi = True

        self.frame_aksi.pack_forget()
        self.btn_start.pack(pady=20)
        self.btn_start.config(text="Cek Laptop Lain")

        if not terdeteksi:
            # 3. PENANGANAN JIKA TIDAK COCOK
            messagebox.showinfo("Hasil", "Selamat! Laptop Anda dalam kondisi sehat.\nTidak ditemukan gejala kerusakan serius.")
        else:
            # 4. OUTPUT NAMA KERUSAKAN & SOLUSI
            messagebox.showwarning("Hasil Diagnosa", f"Hasil Analisis:\n\n{hasil_teks}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LaptopExpert(root)
    root.mainloop()