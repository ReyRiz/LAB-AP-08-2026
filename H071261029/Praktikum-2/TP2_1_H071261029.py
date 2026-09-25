# Tingkat kepedasan makanan

tingkat_persentase = float(input("Masukkan nilai tingkat kepedasan (%): "))

if tingkat_persentase < 0:
    print("Input Tidak Valid")
elif tingkat_persentase <= 10:
    print("Level Aman")
elif tingkat_persentase <= 40:
    print("Level Sedang")
elif tingkat_persentase <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")