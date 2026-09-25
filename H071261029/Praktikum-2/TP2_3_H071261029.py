# seleksi karyawan baru

nilai = float(input("Masukkan nilai tes: "))

if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai >= 65:
    pengalaman_kerja = float(input("Masukkan pengalaman kerja (tahun): "))
    if pengalaman_kerja >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Tidak Lolos")