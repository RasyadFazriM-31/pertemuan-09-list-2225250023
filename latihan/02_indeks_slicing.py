# Latihan 2 - Indeks dan Slicing
# Input  : list enam nilai
# Proses : akses elemen dengan indeks positif, indeks negatif, dan slicing
# Output : elemen pertama, terakhir, tiga elemen awal, dan elemen indeks 1 sampai 3

nilai = [75, 80, 65, 90, 88, 70]
print(nilai[0])      # elemen pertama -> 75
print(nilai[-1])     # elemen terakhir -> 70
print(nilai[:3])     # tiga elemen awal -> [75, 80, 65]
print(nilai[1:4])    # indeks 1 sampai 3 (indeks 4 tidak ikut) -> [80, 65, 90]
