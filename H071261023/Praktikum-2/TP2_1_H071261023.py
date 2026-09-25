level_cabai = int(input("Masukkan persentase cabai :"))

if level_cabai >=0 and level_cabai <=10:
    print ("Level Aman")
elif level_cabai >10 and level_cabai <=40:
    print("Level Sedang")
elif level_cabai >40 and level_cabai <=70:
    print("Level Pedas")
elif level_cabai >70:
    print("Level Ekstrem")
else:
    print("Input tidak valid") 