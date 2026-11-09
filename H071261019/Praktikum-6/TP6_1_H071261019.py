'''Sistem Inventaris Toko Buku "BookNest"'''

inventaris = []
def tambah_buku(inventaris, judul, penulis, harga, stok):

    try:
        harga = int(harga)
        stok = int(stok)
        if harga < 0 or stok < 0:
            print('angka tidak boleh negatif!')
    except ValueError:
        print('harga dan angka harus berupa angka!')
    
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!\n")

def cari_buku(inventaris, kunci):
    kata_kunci = kunci.lower()

    hasil = []
    for buku in inventaris:
        if kata_kunci in buku["judul"].lower():
            hasil.append(buku)
    if hasil:
        print(f"\nHasil pencarian untuk '{kata_kunci}':")
        for i, buku in enumerate(hasil, 1):
            print(f"{i}. Judul  : {buku['judul']}")
            print(f"   Penulis: {buku['penulis']}")
            print(f"   Harga  : Rp{buku['harga']}")
            print(f"   Stok   : {buku['stok']}")
    else:
        print(f"\nBuku dengan kata kunci '{kata_kunci}' tidak ditemukan.")
    print()

def update_stok(inventaris, judul, jumlah):
    print("\n--- Menu Update Stok ---")
    
    buku_ditemukan = False
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            buku_ditemukan = True
            try:
                jumlah = int(jumlah)
                baru_stok = buku["stok"] + jumlah
                
                if baru_stok < 0:
                    print(f"Gagal! Perubahan stok menyebabkan stok menjadi negatif (Stok saat ini: {buku['stok']}).\n")
                else:
                    buku["stok"] = baru_stok
                    print(f"Stok '{buku['judul']}' berkurang {jumlah}. Stok sekarang: {buku['stok']}.\n")
            except ValueError:
                print("Error: Jumlah perubahan stok harus berupa angka bulat!\n")
            break
            
    if not buku_ditemukan:
        print(f"Error: Buku dengan judul '{judul}' tidak ditemukan di inventaris.\n")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("\nInventaris masih kosong.\n")
        return
        
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("\n=====================================")
    print("        RINGKASAN INVENTARIS         ")
    print("=====================================")
    print(f"Jumlah Jenis Buku : {jumlah_jenis}")
    print(f"Total Seluruh Stok: {total_stok}")
    print(f"Total Nilai Aset  : Rp{total_aset}")
    print(f"Buku Termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=====================================\n")

def main():
    print("========================================")
    print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================\n")
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
            harga = input("Harga: ")
            stok = input("Stok awal: ")
            tambah_buku(inventaris, judul, penulis, harga, stok)

        elif pilihan == "2":
            kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan Sistem Inventaris BookNest!")
            break
        else:
            print("Pilihan menu tidak valid. Silakan coba lagi.\n")
main()