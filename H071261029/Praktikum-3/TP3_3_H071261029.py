while True:
    try:
        jumlah_kursi = int(input("Masukkan maksimal kursi bus: "))
        if jumlah_kursi < 0:
            print("Input jumlah kursi tidak boleh negatif")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka")

if jumlah_kursi > 0:
    print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

total_pendapatan = 0

while jumlah_kursi > 0:
    print(f"Sisa kursi: {jumlah_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Input umur harus berupa angka!\n")
        continue

    if umur < 0:
       print("Umur tidak valid!\n")
       continue

    if umur <= 5:
        print("Kategori: Balita - Tiket Gratis (Rp 0)\n")
        harga = 0
    elif umur <= 12:
        print("Kategori: Anak - Harga: Rp 50.000\n")
        harga = 50000
    else:
        print("Kategori: Dewasa - Harga: Rp 100.000\n")
        harga = 100000

    jumlah_kursi -= 1
    total_pendapatan += harga

if jumlah_kursi == 0:
    print("--- Semua Kursi Terisi ---")
    print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")