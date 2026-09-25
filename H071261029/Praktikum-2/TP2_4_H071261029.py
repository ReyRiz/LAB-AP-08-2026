# rekomendasi paket wisata

tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe_pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan: 
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        # paket c
        elif waktu == "Malam":
            if tipe_pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket yang cocok")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi":
            if tipe_pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket B")
            else:
                print("Tidak ada paket yang cocok")
        # paket c
        elif waktu == "Malam":
            if tipe_pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket yang cocok")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        # paket c
        elif waktu == "Malam":
            if tipe_pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket yang cocok")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tidak ada paket yang cocok")