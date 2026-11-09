tujuan = input ("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input ("Masukkan waktu (Pagi/Malam): ")
tipe = input ("Masukkan tipe pengunjung (Anak/Dewasa): ")
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print ("paket rekomendasi : Paket A")
        elif waktu == "Malam" and tipe == "Dewasa":
            print ("paket rekomendasi : Paket c")
        else:
            print ("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            print("paket rekomendasi : Paket B")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("paket rekomendasi : Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("paket rekomendasi : Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
            print("Tidak ada paket yang cocok")