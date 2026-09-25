while True:
    try:
        x = int(input("Masukkan maksimal kursi bus: "))
        if x <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print("Sistem Reservasi PO BUS Dimulai")
sisa_kursi = x
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
        
        if umur < 0:
            print("Umur tidak valid!")
            continue  
        elif umur <= 5:
            print("Kategori: Balita")
            print("Tiket Gratis (Rp 0)")
            harga = 0
        elif umur <= 12:
            harga = 50000
            print(f"Kategori: Anak Harga: Rp {harga}")
        else:
            harga = 100000
            print(f"Kategori: Dewasa Harga: Rp {harga}")
            
        sisa_kursi -= 1
        total_pendapatan += harga
        
    except ValueError:
        print("Input umur harus berupa angka!")

print("Semua Kursi Terisi")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")