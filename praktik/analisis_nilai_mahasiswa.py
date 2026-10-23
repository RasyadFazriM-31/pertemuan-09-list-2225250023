# Praktik Pertemuan 9 - Analisis Nilai Mahasiswa
# Input  : list berisi 10 nilai mahasiswa, batas kelulusan 60
# Proses : hitung statistik dasar, saring nilai yang lulus
# Output : ringkasan statistik dan informasi kelulusan

BATAS_LULUS = 60


def rata_rata(data):
    """Rata-rata list numerik; list kosong dianggap 0 agar aman."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=BATAS_LULUS):
    """Mengembalikan list baru berisi nilai yang >= batas."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil


def tampilkan_ringkasan(nilai):
    lulus = nilai_lulus(nilai)
    print(f"Data          : {nilai}")
    print(f"Banyak data   : {len(nilai)}")
    print(f"Total         : {sum(nilai)}")
    print(f"Rata-rata     : {rata_rata(nilai):.2f}")
    print(f"Minimum       : {min(nilai)}")
    print(f"Maksimum      : {max(nilai)}")
    print(f"Batas lulus   : {BATAS_LULUS}")
    print(f"Nilai lulus   : {lulus}")
    print(f"Jumlah lulus  : {len(lulus)}")
    print(f"Belum lulus   : {len(nilai) - len(lulus)}")


if __name__ == "__main__":
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
    tampilkan_ringkasan(nilai)
