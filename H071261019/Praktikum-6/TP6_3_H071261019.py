'''Sistem Manajemen Playlist Musik "PlayTune"'''

playlist = []
genre_set = set()
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):

    try:
        durasi_detik = int(durasi)
        if durasi_detik < 0:
            print('durasi tidak boleh negatif!\n')
        else:
            lagu = (judul, artis, genre, durasi_detik) 
            playlist.append(lagu)
            genre_set.add(genre)
    except ValueError:
        print('durasi harus berupa angka!\n')

def tampilkan_playlist(playlist):
    print("========================================================")
    print(f" No  Judul                Artis           Genre  Durasi")
    print("========================================================")

    total_detik = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        menit = durasi // 60
        detik = durasi % 60
        durasi_str = f"{menit:02d}:{detik:02d}"
        print(f" {i:<3} {judul:<20} {artis:<15} {genre:<6} {durasi_str}")
        total_detik += durasi

    print("========================================================")
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print(f"Total durasi playlist: {total_menit:02d} menit {sisa_detik:02d} detik\n")

def filter_genre(playlist, genre_target):
    if not genre_set:
        print("Belum ada genre tersedia.\n")
        return

    print(f"\nGenre tersedia: {genre_set}")
    genre_target = input("Masukkan genre yang ingin difilter: ")

    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    
    print(f"\nLagu bergenre '{genre_target}':")
    if hasil:
        for i, (judul, artis, _, durasi) in enumerate(hasil, start=1):
            print(f"   {i}. {judul} - {artis} ({durasi // 60}:{durasi % 60:02d})\n")
    else:
        print("   Tidak ada lagu ditemukan.\n")

def hapus_lagu(playlist, nomor):
    if not playlist:
        print("Playlist kosong.\n")
        return

    tampilkan_playlist(playlist)
    try:
        nomor = int(nomor)
        if nomor >= 1 and nomor <= len(playlist):
            hapus = playlist.pop(nomor-1)
            print(f"Lagu '{hapus[0]}' berhasil dihapus.")
        else:
            print("Lagu tidak valid!")
    except ValueError:
        print("Input tidak valid!")

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print("      STATISTIK PLAYLIST PLAYTUNE       ")
    print("========================================\n")
    total_lagu = len(playlist)
    print(f"Total lagu: {total_lagu}")
    print(f"Jumlah genre: {len(genre_set)}")
    print(f"Daftar genre: {genre_set}")
    
    if total_lagu == 0:
        return

    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    print("\nDistribusi genre:")
    for genre, count in distribusi.items():
        print(f"  {genre}: # ({count})")

    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])

    print(f"\nLagu terpanjang: {lagu_terpanjang[0]} oleh {lagu_terpanjang[1]} ({lagu_terpanjang[3]} detik)")
    print(f"Lagu terpendek: {lagu_terpendek[0]} oleh {lagu_terpendek[1]} ({lagu_terpendek[3]} detik)")
    print("========================================")


def main():
    print("========================================")
    print("       PLAYLIST MUSIK - PLAYTUNE        ")
    print("========================================\n")
    while True:
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
            durasi = input("Durasi (dalam detik): ")
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            filter_genre(playlist, genre_set)

        elif pilihan == "4":
            tampilkan_playlist(playlist)
            try:
                nomor = input("Masukkan nomor lagu yang ingin dihapus: ")
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Tidak valid!")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan menu tidak valid. Silakan coba lagi.\n")
main()