
nilai = int(input("Masukkan nilai tes : "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun) : "))
if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif 65 <= nilai <= 80 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")
