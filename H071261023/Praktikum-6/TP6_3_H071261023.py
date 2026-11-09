print("======================================")
print("     PLAYLIST MUSIK - PLAYTUNE")
print("======================================")

playlist = []
genre_set = set()

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre_formatted = genre.capitalize()
    lagu = (judul, artis, genre_formatted, durasi)
    playlist.append(lagu)
    genre_set.add(genre_formatted)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("\nPlaylist masih kosong!")
        return

    print("=======================================================")
    print(f"{'No':<3} {'Judul':<19} {'Artis':<14} {'Genre':<9} {'Durasi'}")
    print("=======================================================")

    total = 0
    for i, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60
        durasi_str = f"{menit}:{detik:02d}"

        print(f"{i:<3} {judul:<19} {artis:<14} {genre:<9} {durasi_str}")
        total += durasi

    print("=======================================================")
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")

def filter_genre(playlist, genre_target):
    target_lower = genre_target.lower()
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == target_lower
    ]
    return hasil

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        playlist.pop(nomor - 1)
        print("Lagu berhasil dihapus!")
    else:
        print("Nomor lagu tidak ditemukan!")

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print("     STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"Total lagu      : {len(playlist)}")
    print(f"Jumlah genre    : {len(genre_set)}")
    print(f"Daftar genre    : {genre_set}")

    if not playlist:
        print("Playlist masih kosong!")
        print("========================================")
        return

    jumlah_genre = {}
    for lagu in playlist:
        g = lagu[2]
        jumlah_genre[g] = jumlah_genre.get(g, 0) + 1

    print("Distribusi genre:")
    for g, jumlah in jumlah_genre.items():
        print(f"{g:<12}: {'#' * jumlah} ({jumlah})")

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    p_menit, p_detik = terpanjang[3] // 60, terpanjang[3] % 60
    pend_menit, pend_detik = terpendek[3] // 60, terpendek[3] % 60

    print(f"Lagu terpanjang : {terpanjang[0]} ({p_menit}:{p_detik:02d})")
    print(f"Lagu terpendek  : {terpendek[0]} ({pend_menit}:{pend_detik:02d})")
    print("========================================")

# Loop Menu Utama
while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilih = input("Pilih menu (1-6): ")

    if pilih == "1":
        judul = input("Judul lagu: ")
        artis = input("Nama artis: ")
        genre = input("Genre: ")

        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi > 0:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            else:
                print("Durasi harus lebih dari 0!")
        except ValueError:
            print("Durasi harus berupa angka!")

    elif pilih == "2":
        tampilkan_playlist(playlist)

    elif pilih == "3":
        if not genre_set:
            print("Belum ada genre tersedia.")
        else:
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ")
            hasil_filter = filter_genre(playlist, target)
            
            print(f"Lagu bergenre '{target.capitalize()}':")
            for i, lagu in enumerate(hasil_filter, start=1):
                menit = lagu[3] // 60
                detik = lagu[3] % 60
                print(f"{i}. {lagu[0]} - {lagu[1]} ({menit}:{detik:02d})")

    elif pilih == "4":
        if not playlist:
            print("Playlist kosong!")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("Nomor lagu yang dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Masukkan nomor yang benar!")

    elif pilih == "5":
        statistik_playlist(playlist, genre_set)

    elif pilih == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak tersedia!")