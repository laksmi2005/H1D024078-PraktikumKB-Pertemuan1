import tkinter as tk
from tkinter import messagebox

database_tht = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

daftar_gejala = [
    ("G1", "nafas abnormal"), ("G2", "suara serak"), ("G3", "perubahan kulit"),
    ("G4", "telinga penuh"), ("G5", "nyeri bicara menelan"), ("G6", "nyeri tenggorokan"),
    ("G7", "nyeri leher"), ("G8", "pendarahan hidung"), ("G9", "telinga berdenging"),
    ("G10", "airliur menetes"), ("G11", "perubahan suara"), ("G12", "sakit kepala"),
    ("G13", "nyeri pinggir hidung"), ("G14", "serangan vertigo"), ("G15", "getah bening"),
    ("G16", "leher bengkak"), ("G17", "hidung tersumbat"), ("G18", "infeksi sinus"),
    ("G19", "beratbadan turun"), ("G20", "nyeri telinga"), ("G21", "selaput lendir merah"),
    ("G22", "benjolan leher"), ("G23", "tubuh tak seimbang"), ("G24", "bolamata bergerak"),
    ("G25", "nyeri wajah"), ("G26", "dahi sakit"), ("G27", "batuk"),
    ("G28", "tumbuh dimulut"), ("G29", "benjolan dileher"), ("G30", "nyeri antara mata"),
    ("G31", "radang gendang telinga"), ("G32", "tenggorokan gatal"), ("G33", "hidung meler"),
    ("G34", "tuli"), ("G35", "mual muntah"), ("G36", "letih lesu"), ("G37", "demam")
]

class THTExpertInLine:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar THT - H1H024035")
        self.root.geometry("500x300")
        
        self.gejala_terpilih = []
        self.index = 0

        self.main_frame = tk.Frame(root)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lbl_tanya = tk.Label(self.main_frame, text="Klik tombol Mulai untuk Diagnosa", wraplength=450, pady=20, font=("Arial", 10))
        self.lbl_tanya.pack()

        self.btn_start = tk.Button(self.main_frame, text="Mulai", width=15, bg="#3498db", fg="white", font=("Arial", 10, "bold"), command=self.mulai)
        self.btn_start.pack()

        self.frame_aksi = tk.Frame(self.main_frame)
        self.btn_ya = tk.Button(self.frame_aksi, text="YA", width=10, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_aksi, text="TIDAK", width=10, bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=lambda: self.jawab('t'))

    def mulai(self):
        self.gejala_terpilih = []
        self.index = 0
        self.btn_start.pack_forget()
        self.frame_aksi.pack(pady=20)
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)
        self.update_pertanyaan()

    def update_pertanyaan(self):
        if self.index < len(daftar_gejala):
            self.lbl_tanya.config(text=f"Apakah Anda mengalami gejala {daftar_gejala[self.index][1]}?")
        else:
            self.tampilkan_hasil()

    def jawab(self, p):
        if p == 'y': self.gejala_terpilih.append(daftar_gejala[self.index][0])
        self.index += 1
        self.update_pertanyaan()

    def tampilkan_hasil(self):
        hasil = [p for p, g in database_tht.items() if all(x in self.gejala_terpilih for x in g)]
        self.frame_aksi.pack_forget()
        self.btn_start.pack()
        self.btn_start.config(text="Cek Lagi")
        
        msg = "\n".join(hasil) if hasil else "Gejala tidak cocok dengan penyakit manapun."
        messagebox.showinfo("Hasil", f"Penyakit terdeteksi:\n\n{msg}")
        self.lbl_tanya.config(text="Diagnosa Selesai.")

if __name__ == "__main__":
    root = tk.Tk()
    app = THTExpertInLine(root)
    root.mainloop()