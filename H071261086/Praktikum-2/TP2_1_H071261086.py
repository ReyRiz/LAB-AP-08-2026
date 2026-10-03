persentase_cabai = float(input("Masukkan persentase cabai: "))

if persentase_cabai < 0:
    print("Persentase tidak boleh negatif!")
elif persentase_cabai >= 0 and persentase_cabai <= 10:
    print("Level aman")
elif persentase_cabai >= 11 and persentase_cabai <= 40:
    print("Level sedang")
elif persentase_cabai >= 41 and persentase_cabai <= 70:
    print("Level pedas")
elif persentase_cabai > 70 and persentase_cabai <= 100:
    print("Level ekstrem")
else:
    print("Persentase tidak lebih dari 100!")

