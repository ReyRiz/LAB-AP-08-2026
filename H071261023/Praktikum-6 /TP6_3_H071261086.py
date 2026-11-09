def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")
    print()

def format_menit_detik(detik):
    menit = detik // 60
    sisa = detik % 60
    return f"{menit}:{sisa:02d}"

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist kosong.")
        print()
        return

    print("======================================================================")
    print(f"{'No':<3} {'Judul':<20} {'Artis':<20} {'Genre':<15} {'Durasi'}")
    print("======================================================================")
    
    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        durasi_str = format_menit_detik(durasi)
        print(f"{i:<3} {judul:<20} {artis:<20} {genre:<15} {durasi_str}")
    
    print("======================================================================")
    total_menit = total_detik // 60
    total_sisa = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {total_sisa} detik")
    print()

def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_hapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_hapus[0]}' berhasil dihapus dari playlist!")
    else:
        print("Error: Nomor lagu tidak valid!")
    print()

def statistik_playlist(playlist, genre_set):
    print("===================================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("===================================")
    
    if not playlist:
        print("Playlist kosong.")
        print("===================================")
        print()
        return

    print(f"Total lagu     : {len(playlist)}")
    print(f"Jumlah genre   : {len(genre_set)}")
    print(f"Daftar genre   : {genre_set}")
    print()
    
    
    distribusi = {}
    for lagu in playlist:
        g = lagu[2]
        distribusi[g] = distribusi.get(g, 0) + 1
    
    print("Distribusi genre:")
    for genre, jumlah in distribusi.items():
        bar = "# " * 0 + "# (" + str(jumlah) + ")"  
        print(f"  {genre:<8} : {bar}")
    
    print()
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    print(f"Lagu terpanjang : {lagu_terpanjang[0]} ({format_menit_detik(lagu_terpanjang[3])})")
    print(f"Lagu terpendek  : {lagu_terpendek[0]} ({format_menit_detik(lagu_terpendek[3])})")
    print("===================================")
    print()

def main():
    playlist = []
    genre_set = set()
    
    print("===================================")
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("===================================")
    print()

    while True:
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        pilih = input("Pilih menu (1-6): ")

        if pilih == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Error: Durasi harus angka positif!")
                    print()
                    continue
            except ValueError:
                print("Error: Durasi harus berupa angka!")
                print()
                continue
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

        elif pilih == "2":
            tampilkan_playlist(playlist)

        elif pilih == "3":
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ")
            hasil = filter_genre(playlist, target)
            if hasil:
                print(f"\nLagu bergenre '{target}':")
                for i, lagu in enumerate(hasil, 1):
                    print(f"  {i}. {lagu[0]} - {lagu[1]} ({format_menit_detik(lagu[3])})")
            else:
                print(f"Tidak ada lagu dengan genre '{target}'.")
            print()

        elif pilih == "4":
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])
                except ValueError:
                    print("Error: Nomor harus berupa angka!")
                    print()

        elif pilih == "5":
            statistik_playlist(playlist, genre_set)

        elif pilih == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid!")
            print()

if __name__ == "__main__":
    main()
