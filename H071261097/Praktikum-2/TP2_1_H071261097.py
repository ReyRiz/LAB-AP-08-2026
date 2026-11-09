#Nomor 1
cabai = int(input("masukkan persentase cabai: "))
if cabai >= 0 and cabai <= 10:
    print("Level Aman")
elif cabai >= 11 and cabai <= 40:
    print("Level Sedang")
elif cabai >= 41 and cabai <= 70:
    print("Level Pedas")
elif cabai >= 71:
    print("Level Ekstrim")
else:
    print("Input tidak valid")