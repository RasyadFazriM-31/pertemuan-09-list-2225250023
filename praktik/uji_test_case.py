# Pengujian test case wajib Pertemuan 9 (otomatis, memakai assert)
# Jalankan dari folder utama: python3 praktik/uji_test_case.py

from analisis_nilai_mahasiswa import rata_rata, nilai_lulus

# [60, 70, 80]
data = [60, 70, 80]
assert f"{rata_rata(data):.2f}" == "70.00"
assert (min(data), max(data)) == (60, 80)
assert len(nilai_lulus(data)) == 3

# [59, 60, 61] -> batas kelulusan 60: 2 lulus
assert len(nilai_lulus([59, 60, 61])) == 2

# [] -> tidak error
assert rata_rata([]) == 0

print("Semua test case Pertemuan 9 LULUS")
