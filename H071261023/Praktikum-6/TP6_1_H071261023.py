print("======================================")
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("======================================")
inventaris = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print("Buku berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            print(buku)

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            if buku["stok"] + jumlah >= 0:
                buku["stok"] += jumlah
                print("Stok berhasil diupdate!")
            else:
                print("Gagal! Stok tidak boleh negatif.")
            return
    print("Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    print("\n========================================")
    print("     RINGKASAN INVENTARIS BOOKNEST ")
    print("========================================")
    print("Jumlah jenis buku:", len(inventaris))

    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print("Total seluruh stok:", total_stok)
    print("Total nilai aset: Rp", total_aset)

    if len(inventaris) > 0:
        termahal = max(inventaris, key=lambda buku: buku["harga"])
        print("Buku termahal:", termahal["judul"])

    print("========================================")

while True:
    print("\nmenu: ")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilih = input("Pilih menu (1-5): ")

    if pilih == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)

        except ValueError:
            print("Harga dan stok harus berupa angka!")

    elif pilih == "2":
        kata_kunci = input("Cari judul buku: ")
        cari_buku(inventaris, kata_kunci)

    elif pilih == "3":
        judul = input("Judul buku: ")

        try:
            jumlah = int(input("Perubahan stok (+/-): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Masukkan angka yang benar!")

    elif pilih == "4":
        ringkasan_inventaris(inventaris)

    elif pilih == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak tersedia!")