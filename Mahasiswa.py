# Program sederhana untuk menentukan mahasiswa terbaik
# Data mahasiswa (nama, IPK, prestasi, public speaking, etika)

mahasiswa = [
    {"nama": "Budi", "ipk": 3.80, "prestasi": 2, "public_speaking": 75, "etika": 85},
    {"nama": "Anya", "ipk": 3.90, "prestasi": 0, "public_speaking": 82, "etika": 80},
    {"nama": "Juned", "ipk": 4.00, "prestasi": 3, "public_speaking": 70, "etika": 79},
]

# Hitung skor total sederhana (bobot bisa disesuaikan)
for m in mahasiswa:
    m["skor_total"] = (
        (m["ipk"] * 25) +
        (m["prestasi"] * 10) +
        (m["public_speaking"] * 0.3) +
        (m["etika"] * 0.2)
    )

# Cari mahasiswa terbaik
mahasiswa_terbaik = max(mahasiswa, key=lambda x: x["skor_total"])

print("=== Daftar Mahasiswa ===")
for m in mahasiswa:
    print(f"{m['nama']} - Skor: {m['skor_total']:.2f}")

print("\nMahasiswa terbaik adalah:", mahasiswa_terbaik["nama"])
