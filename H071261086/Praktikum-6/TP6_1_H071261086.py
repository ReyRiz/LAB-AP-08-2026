def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        for i, buku in enumerate(hasil, 1):
            print(f"  {i}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
    else:
        print(f"Tidak ditemukan buku dengan kata kunci '{kata_kunci}'.")
    print()

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            if buku["stok"] + jumlah < 0:
                print("Gagal update stok. Stok tidak boleh negatif!")
                print()
                return
            
            buku["stok"] += jumlah
            if jumlah >= 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
            else:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            print()
            return
    
    print(f"Error: Buku dengan judul '{judul}' tidak ditemukan.")
    print()

def ringkasan_inventaris(inventaris):
    print("===================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("===================================")
    
    if not inventaris:
        print("Inventaris kosong.")
        print()
        return

    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal   : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print()

# Program Utama
def main():
    inventaris = []
    print("===================================")
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("===================================")
    print()

    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Error: Harga dan stok tidak boleh negatif!")
                    print()
                    continue
            except ValueError:
                print("Error: Harga dan stok harus berupa angka!")
                print()
                continue
            tambah_buku(inventaris, judul, penulis, harga, stok)

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            except ValueError:
                print("Error: Jumlah harus berupa angka!")
                print()
                continue
            update_stok(inventaris, judul, jumlah)

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid!")
            print()

if __name__ == "__main__":
    main()
