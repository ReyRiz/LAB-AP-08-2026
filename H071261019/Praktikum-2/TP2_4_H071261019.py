
tujuan = str(input("Masukkan tujuan (Pantai/Pegunungan/Kota) : "))
waktu = str(input("Masukkan waktu (Pagi/Malam) : "))
pengunjung = str(input("Masukkan tipe pengunjung (Anak/Dewasa) : "))
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")  
    case _ :
        print("Tidak ada paket yang cocok")