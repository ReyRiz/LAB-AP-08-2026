#TUGAS 3
while True:
    try:
        jumlah_kursi = int(input("Masukkan maksimal kursi bus: "))
    except:
            print("Input jumlah kursi harus berupa angka!")
    else:
        break

print()
print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = jumlah_kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print()
    print(f"Sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
            print("Umur tidak valid!")
            continue
    elif umur <= 5:
        kategori ="Balita"
        harga = 0
        print(f"Kategori: {kategori} - Tiket Gratis (Rp {harga})")
    elif umur <= 12:
        kategori ="Anak"
        harga = 50000
        print(f"Kategori: {kategori} - Harga: Rp {harga:,}".replace(",","."))
    else:
        kategori ="Dewasa"
        harga = 100000
        print(f"Kategori: {kategori} - Harga: Rp {harga:,}".replace(",","."))

    total_pendapatan += harga
    sisa_kursi -= 1

print()
print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,}".replace(",","."))