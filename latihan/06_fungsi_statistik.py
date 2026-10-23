# Latihan 6 - Fungsi Statistik
# Input  : list nilai sebagai parameter fungsi
# Proses : hitung rata-rata; list kosong dikembalikan 0 agar tidak ZeroDivisionError
# Output : rata-rata dengan dua angka desimal


def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")
