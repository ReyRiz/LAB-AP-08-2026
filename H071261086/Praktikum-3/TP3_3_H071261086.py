print("--- Sistem Reservasi PO BUS ---")

while True:
    try:
        kursi = int(input("Masukkan jumlah kursi bus: "))
        if kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
        break
    except ValueError:
        print("Input harus berupa angka!")

sisa_kursi = kursi
total_pendapatan = 0
penumpang_ke = 1

while sisa_kursi > 0:
    try:
        umur = int(input(f"Masukkan umur penumpang ke {penumpang_ke}: "))
    except ValueError:
        print("Umur tidak valid!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur and umur <= 5:
        harga = 0
        kategori = "Gratis"
    elif umur <= 12:
        harga = 50000
        kategori = "Tiket Anak"
    else:
        harga = 100000
        kategori = "Tiket Dewasa"

    total_pendapatan += harga
    sisa_kursi -= 1
    
    print(f"-> {kategori} (Rp {harga}) - Sisa kursi: {sisa_kursi}")
    penumpang_ke += 1

print(f"Bus penuh! Total pendapatan: Rp {total_pendapatan}")
