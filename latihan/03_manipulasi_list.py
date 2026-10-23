# Latihan 3 - Manipulasi List
# Input  : list tiga nilai
# Proses : ubah, tambah, sisipkan, dan hapus elemen
# Output : list setelah seluruh perubahan

nilai = [75, 80, 65]
nilai[1] = 82        # [75, 82, 65]
nilai.append(90)     # [75, 82, 65, 90]
nilai.insert(1, 70)  # [75, 70, 82, 65, 90]
nilai.remove(65)     # [75, 70, 82, 90]
print(nilai)
