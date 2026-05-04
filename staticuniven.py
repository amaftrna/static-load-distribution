import random

# ==========================================
# SIMULASI STATIC UNEVEN DISTRIBUTION
# NRP GENAP VERSION (CUSTOM LOGIC)
# ==========================================

# 1. Generate daftar task (beban kerja)
jumlah_task = 12
tasks = [random.randint(2, 9) for _ in range(jumlah_task)]

# 2. Inisialisasi 3 processor
processor = {
    "P1": 0,
    "P2": 0,
    "P3": 0
}

print("=== DATA TASK ===")
print(tasks)
print("\n=== PROSES DISTRIBUSI (STATIC UNEVEN) ===")

# 3. Distribusi tidak merata dengan pola custom
for i, nilai in enumerate(tasks):
    
    # aturan unik:
    # - index 0,4,8,... → P1
    # - index 1,5,9,... → P2
    # - sisanya → P3
    
    if i % 4 == 0:
        processor["P1"] += nilai
        print(f"Task ke-{i} ({nilai}) → P1")
    
    elif i % 4 == 1:
        processor["P2"] += nilai
        print(f"Task ke-{i} ({nilai}) → P2")
    
    else:
        processor["P3"] += nilai
        print(f"Task ke-{i} ({nilai}) → P3")

# 4. Tampilkan hasil distribusi
print("\n=== HASIL AKHIR LOAD ===")
for key, value in processor.items():
    print(f"{key} menanggung beban: {value}")

# 5. Hitung distribusi ideal
total_beban = sum(tasks)
ideal = total_beban / len(processor)

print("\nTotal beban:", total_beban)
print("Target ideal per processor:", round(ideal, 2))

# 6. Analisis selisih terhadap ideal
print("\n=== ANALISIS KESEIMBANGAN ===")
mendekati = True

for key, value in processor.items():
    selisih = abs(value - ideal)
    print(f"{key} selisih dari ideal: {round(selisih,2)}")
    
    # jika selisih terlalu jauh, tandai tidak ideal
    if selisih > 4:
        mendekati = False

# 7. Kesimpulan otomatis
print("\n=== KESIMPULAN ===")
if mendekati:
    print("Distribusi SUDAH mendekati kondisi IDEAL ✅")
else:
    print("Distribusi MASIH belum merata ❌")