# Latihan 5 - Filter Kelulusan
# Input  : list nilai, batas kelulusan 60
# Proses : telusuri tiap nilai, simpan yang >= 60 ke list baru
# Output : daftar nilai lulus dan jumlahnya

nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
