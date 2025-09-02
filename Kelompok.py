# Data mahasiswa: nama, id_kelompok, ipk, prestasi, public speaking, etika
mahasiswa = [
    {"nama": "Ana", "kelompok": 1, "ipk": 3.80, "prestasi": 2, "public_speaking": 75, "etika": 85},
    {"nama": "Anya", "kelompok": 1, "ipk": 3.90, "prestasi": 0, "public_speaking": 82, "etika": 80},
    {"nama": "Juned", "kelompok": 2, "ipk": 4.00, "prestasi": 3, "public_speaking": 70, "etika": 79},
    {"nama": "Sinta", "kelompok": 2, "ipk": 3.70, "prestasi": 1, "public_speaking": 88, "etika": 84},
    {"nama": "Rizky", "kelompok": 3, "ipk": 3.60, "prestasi": 2, "public_speaking": 80, "etika": 90},
    {"nama": "Maya", "kelompok": 3, "ipk": 3.75, "prestasi": 1, "public_speaking": 85, "etika": 87},
]

# Fungsi hitung skor tiap mahasiswa
def hitung_skor(m):
    # bobot (bisa disesuaikan)
    return (m["ipk"] * 25) + (m["prestasi"] * 10) + (m["public_speaking"] * 0.3) + (m["etika"] * 0.2)

# Fungsi hitung peringkat kelompok
def hitung_peringkat_kelompok():
    kelompok_skor = {}

    for m in mahasiswa:
        skor = hitung_skor(m)
        if m["kelompok"] not in kelompok_skor:
            kelompok_skor[m["kelompok"]] = []
        kelompok_skor[m["kelompok"]].append(skor)

    # rata-rata skor tiap kelompok
    hasil = []
    for k, nilai in kelompok_skor.items():
        avg = sum(nilai) / len(nilai)
        hasil.append({"kelompok": k, "skor": avg})

    # urutkan dari yang tertinggi
    urut = sorted(hasil, key=lambda x: x["skor"], reverse=True)
    return urut

if __name__ == "__main__":
    print("=== PERINGKAT KELOMPOK ===")
    for i, k in enumerate(hitung_peringkat_kelompok(), start=1):
        print(f"{i}. Kelompok {k['kelompok']} - Rata-rata Skor: {k['skor']:.2f}")
