def tambah_buku(inventaris: list, judul: str, penulis: str, harga: int, stok: int) -> bool:
    if harga < 0 or stok < 0:
        print(">> Error: Harga dan stok tidak boleh bernilai negatif!")
        return False

    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku_baru)
    print(f">> Buku '{judul}' berhasil ditambahkan ke inventaris!")
    return True

def cari_buku(inventaris: list, kata_kunci: str) -> list:
    hasil_pencarian = []
    kata_kunci_kecil = kata_kunci.lower()

    for buku in inventaris:
        if kata_kunci_kecil == buku["judul"].lower():
            hasil_pencarian.append(buku)

    return hasil_pencarian

def update_stok(inventaris: list, judul: str, jumlah: int) -> bool:
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f">> Error: Stok tidak mencukupi! Stok saat ini:{buku['stok']}")
                return False

            if jumlah < 0:
                keterangan = "berkurang"
                angka = jumlah * -1
            else:
                keterangan = "bertambah"
                angka = jumlah
            
            buku["stok"] = stok_baru
            print(f">> Stok buku '{buku['judul']}' {keterangan} {angka}. Stok sekarang: {stok_baru}!")
            return True

    print(f">> Error: Buku dengan judul '{judul}' tidak ditemukan!")
    return False

def ringkasan_inventaris(inventaris: list) -> None:
    if not inventaris:
        print(">> Inventaris masih kosong.")
        return

    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)

    buku_termahal = max(inventaris, key=lambda b: b["harga"])

    print("========================================")
    print("RINGKASAN INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")


inventaris_buku = []

while True:
    print("\n========================================")
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("========================================")
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        print("\n--- TAMBAH BUKU ---")
        judul = input("Masukkan judul buku : ").strip()
        penulis = input("Masukkan nama penulis: ").strip()

        try:
            harga = int(input("Masukkan harga buku: "))
            stok = int(input("Masukkan stok awal: "))
            tambah_buku(inventaris_buku, judul, penulis, harga, stok)
        except ValueError:
            print(">> Error: Harga dan stok harus berupa angka bulat!")

    elif pilihan == "2":
        print("\n--- CARI BUKU ---")
        kata_kunci = input("Masukkan kata kunci judul: ").strip()
        hasil = cari_buku(inventaris_buku, kata_kunci)

        if hasil:
            print(f"\n>> Ditemukan {len(hasil)} buku yang cocok:")
            for idx, buku in enumerate(hasil, 1):
                print(f"{idx}. {buku['judul']} | Penulis: {buku['penulis']} | Harga: Rp{buku['harga']} | Stok: {buku['stok']}")
        else:
            print(">> Tidak ada buku yang cocok dengan kata kunci tersebut.")

    elif pilihan == "3":
        print("\n--- UPDATE STOK ---")
        judul = input("Masukkan judul buku: ").strip()
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris_buku, judul, jumlah)
        except ValueError:
            print(">> Error: Perubahan stok harus berupa angka!")

    elif pilihan == "4":
        print("\n--- RINGKASAN INVENTARIS ---")
        ringkasan_inventaris(inventaris_buku)

    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan BookNest!")
        break

    else:
        print(">> Pilihan menu tidak valid. Silahkan pilih 1-5.")