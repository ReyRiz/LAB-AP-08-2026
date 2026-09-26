#opsi 2 ga ada tulisan kursi kosong
print("--- Setup Denah Bioskop NontonYok ---")


while True:
    try:
        jumlah_baris = int(input("Masukkan jumlah baris: "))
        if jumlah_baris < 0:
            print("Jumlah baris harus lebih dari 0!\n")
            print()
            continue
        break
    except:
        print("Input baris harus berupa angka!")
        print()

         

while True:
    try:
        jumlah_kursi = int(input("Masukkan jumlah kursi per baris: "))
    except:
            print("Input kursi harus berupa angka!")
    else:
        if jumlah_kursi < 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break

print()
print ("--- Daftar Kursi Tersedia ---")

for baris in range (1, jumlah_baris + 1):
    for kursi in range (1, jumlah_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0 :
            continue
        print(f"Baris {baris} - Kursi {kursi}")