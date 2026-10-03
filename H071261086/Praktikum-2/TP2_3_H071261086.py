nilai_tes = int(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai_tes >= 80:
    print("Lolos ke tahap wawancara")
elif nilai_tes < 80 and nilai_tes >= 65 and pengalaman >= 2:
    print("Lolos bersyarat")
else:
    print("Tidak lolos")
