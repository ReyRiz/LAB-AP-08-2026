print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        a = int(input("masukkan jumlah baris: "))
        if a <= 0:
            print("jumlah baris harus lebih dari 0: ")
            continue
        break
    except ValueError:
        print("input harus berupa angka")

while True:
    try:
        b = int(input("masukkan jumlah kursi per baris: "))
        if b <= 0:
            print("jumlah kursi harus lebih dari 0: ")
            continue
        break
    except ValueError:
        print("input harus berupa angka")

print("--- daftar kursi tersedia ---")
for baris in range(1, a, 1):
    for kursi in range(1, b, 1):
        if kursi == 13:
            continue
        if baris == 1:
            if kursi % 2 == 0:
                continue
        print(f"baris {baris} - kursi {kursi}")
