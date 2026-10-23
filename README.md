# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

## Tujuan

Mengolah kumpulan data numerik dengan list Python: akses elemen, manipulasi, perulangan, agregasi, dan fungsi yang menerima list.

## Struktur Program

```
pertemuan-09-list-2225250023/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_buat_list.py          membuat dan membaca list
|   |-- 02_indeks_slicing.py     indeks positif/negatif dan slicing
|   |-- 03_manipulasi_list.py    ubah, append, insert, remove
|   |-- 04_agregasi_nilai.py     total, rata-rata, min, maks
|   |-- 05_filter_kelulusan.py   saring nilai >= 60
|   `-- 06_fungsi_statistik.py   fungsi rata_rata dengan penanganan list kosong
`-- praktik/
    |-- analisis_nilai_mahasiswa.py   praktik inti
    `-- uji_test_case.py              pengujian test case wajib (assert)
```

## Cara Menjalankan

```
python3 praktik/analisis_nilai_mahasiswa.py
```

Untuk menguji test case wajib:

```
cd praktik
python3 uji_test_case.py
```

(Pada Windows gunakan `python` sebagai pengganti `python3`.)

## Hasil Latihan

| Latihan | Hasil yang ditampilkan |
|---|---|
| 01 | `[75, 80, 65, 90, 88]` dan `Banyak data = 5` |
| 02 | `75`, `70`, `[75, 80, 65]`, `[80, 65, 90]` |
| 03 | `[75, 70, 82, 90]` |
| 04 | Total 398, rata-rata 79.60, minimum 65, maksimum 90 |
| 05 | Nilai lulus `[75, 80, 60, 90]`, jumlah lulus 4 |
| 06 | Rata-rata 79.60 |

## Algoritma Praktik

1. Siapkan list berisi 10 nilai.
2. Hitung banyak data dengan `len`.
3. Hitung total, minimum, maksimum, dan rata-rata (`sum(data) / len(data)`).
4. Telusuri setiap nilai; jika `>= 60`, tambahkan ke list `lulus`.
5. Jumlah belum lulus = banyak data dikurangi jumlah lulus.
6. Tampilkan seluruh hasil.

Hasil untuk data `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]`: total 695, rata-rata 69.50, minimum 45, maksimum 90, lulus 7 orang (`[78, 90, 67, 60, 82, 71, 88]`), belum lulus 3 orang.

## Test Case

| Data | Yang diperiksa | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| [60, 70, 80] | Rata-rata | 70.00 | 70.00 | Lulus |
| [60, 70, 80] | Minimum / maksimum | 60 / 80 | 60 / 80 | Lulus |
| [60, 70, 80] | Jumlah lulus | 3 | 3 | Lulus |
| [59, 60, 61] | Batas kelulusan | 2 lulus | 2 lulus | Lulus |
| [] | Fungsi rata_rata | Tidak error | 0 (tidak error) | Lulus |

## Refleksi

indeks list dimulai dari 0, dan pada slicing `nilai[1:4]` batas akhir (indeks 4) tidak ikut diambil. Satu kesalahan yang perlu dihindari: menghitung rata-rata dari list kosong menyebabkan `ZeroDivisionError`, sehingga fungsi `rata_rata` memeriksa `len(data) == 0` terlebih dahulu.

## Sumber dan Bantuan

Bahan ajar Pertemuan 9 (Dr. Aan Hendrayana, S.Si., M.Pd.). Kerangka kode dan README dibantu oleh Claude (AI); seluruh kode telah dijalankan dan diuji.
