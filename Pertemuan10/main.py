import random
import matplotlib.pyplot as plt
import numpy as np

# Mengimpor fungsi-fungsi dari file lain
from inisiasipopulasi import inisialisasi_populasi
from evaluasifitness import hitung_fitness
from selection import tournament_selection       # Sesuai digit ke-1 dari akhir NIM (7) -> TS
from crossover import uniform_crossover          # Sesuai digit ke-2 dari akhir NIM (8) -> Uniform
from mutation import uniform_mutation            # Sesuai hasil 7+8=15 (digit terakhir 5) -> Uniform

# Data barang: (nama, keuntungan, ukuran) sesuai gambar tugas 10
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

def run_ga(jumlah_generasi, jumlah_populasi, prob_crossover, prob_mutasi, kapasitas_tas):
    # Menentukan jumlah gen berdasarkan jumlah barang
    jumlah_gen = len(barang)
    
    # Inisialisasi populasi awal
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    # List untuk menyimpan nilai fitness terbaik, terburuk, dan rata-rata setiap generasi
    best_fitness_list = []
    worst_fitness_list = []
    avg_fitness_list = []
    all_fitness = []
    
    # Variabel untuk menyimpan individu terbaik secara keseluruhan
    best_individu = None
    best_fitness_overall = -1
    
    # Proses evolusi selama jumlah generasi yang ditentukan
    for generasi in range(jumlah_generasi):
        # Evaluasi fitness populasi saat ini
        fitness_populasi = [hitung_fitness(individu, barang, kapasitas_tas) for individu in populasi]
        
        # Menyimpan nilai fitness untuk plotting
        best_fitness = max(fitness_populasi)
        worst_fitness = min(fitness_populasi)
        avg_fitness = sum(fitness_populasi) / len(fitness_populasi)
        
        best_fitness_list.append(best_fitness)
        worst_fitness_list.append(worst_fitness)
        avg_fitness_list.append(avg_fitness)
        all_fitness.append(fitness_populasi.copy())
        
        # Menyimpan individu terbaik secara keseluruhan
        if best_fitness > best_fitness_overall:
            best_fitness_overall = best_fitness
            index_best = fitness_populasi.index(best_fitness)
            best_individu = populasi[index_best].copy()
            
        new_populasi = []
        
        # Membentuk populasi baru
        while len(new_populasi) < jumlah_populasi:
            # 1. SELEKSI: Menggunakan Tournament Selection (Digit 7)
            parent1, idx1 = tournament_selection(populasi, fitness_populasi)
            
            # Membuat list populasi alternatif tanpa parent1 agar parent tidak kembar
            available_populasi = [p for i, p in enumerate(populasi) if i != idx1]
            available_fitness = [f for i, f in enumerate(fitness_populasi) if i != idx1]
            
            # Jika populasi habis (kondisi ekstrem), gunakan populasi utuh
            if not available_populasi:
                available_populasi = populasi.copy()
                available_fitness = fitness_populasi.copy()
                
            parent2, _ = tournament_selection(available_populasi, available_fitness)
            
            # 2. CROSSOVER: Menggunakan Uniform Crossover (Digit 8)
            if random.random() < prob_crossover:
                anak1, anak2 = uniform_crossover(parent1, parent2)
            else:
                anak1, anak2 = parent1[:], parent2[:]
                
            # 3. MUTASI: Menggunakan Uniform Mutation (Digit 5 dari hasil 7+8=15)
            anak1 = uniform_mutation(anak1, mutation_rate=prob_mutasi)
            anak2 = uniform_mutation(anak2, mutation_rate=prob_mutasi)
                
            # Menambahkan anak ke populasi baru
            new_populasi.extend([anak1, anak2])
            
        # Memastikan populasi baru sesuai dengan jumlah populasi
        populasi = new_populasi[:jumlah_populasi]
        
    # Menampilkan grafik fitness
    plt.figure(figsize=(12, 7))
    
    # Plot semua nilai fitness dengan transparansi rendah
    for i in range(jumlah_generasi):
        x = [i+1]*len(all_fitness[i])
        y = all_fitness[i]
        plt.scatter(x, y, color='gray', alpha=0.1)
        
    # Plot nilai fitness terbaik, terburuk, dan rata-rata
    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', label='Fitness Tertinggi')
    plt.plot(range(1, jumlah_generasi+1), worst_fitness_list, color='yellow', label='Fitness Terendah')
    plt.plot(range(1, jumlah_generasi+1), avg_fitness_list, color='red', label='Fitness Rata-rata')
    
    plt.title('Perkembangan Nilai Fitness - NIM H1D024078')
    plt.xlabel('Generasi')
    plt.ylabel('Nilai Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Menampilkan barang yang terpilih dalam knapsack terbaik
    selected_items = [barang[i][0] for i in range(len(best_individu)) if best_individu[i] == 1]
    selected_value = hitung_fitness(best_individu, barang, kapasitas_tas)
    selected_weight = sum([barang[i][2] for i in range(len(best_individu)) if best_individu[i] == 1])
    
    print("=== HASIL OPTIMASI GUDANG ===")
    print(f"Nilai Keuntungan Terbaik : {selected_value}")
    print(f"Total Ukuran Dipakai     : {selected_weight} / {kapasitas_tas}")
    print("Barang Terpilih:")
    for item in selected_items:
        print(f"- {item}")

# Menjalankan GA dengan parameter sesuai instruksi modul
run_ga(
    jumlah_generasi=50,
    jumlah_populasi=20,
    prob_crossover=0.5,
    prob_mutasi=0.1,
    kapasitas_tas=15  # Ukuran Maksimal Gudang tugas 10
)