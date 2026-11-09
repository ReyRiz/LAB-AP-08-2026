#Nomor 3
nilai_tes = int(input("masukkan nilai tes: "))
pengalaman_kerja = int(input("masukkan pengalaman kerja (tahun): "))

if nilai_tes >= 80 and nilai_tes <= 100:
    print("Lolos ke tahap wawancara")
else:
    if pengalaman_kerja >= 2 and nilai_tes >= 65:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")