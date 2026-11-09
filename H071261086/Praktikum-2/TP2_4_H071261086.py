tujuan = input("Pilih tujuan anda (pantai/pegunungan/kota): ")
waktu = input("Pilih waktu (pagi/malam): ")
tipe = input("Tipe pengunjung (dewasa/anak): ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("Rekomendasi paket A")
        elif waktu == "malam" and tipe == "dewasa":
            print("Rekomendasi paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            print("Rekomendasi paket B")
        elif waktu == "malam" and tipe == "dewasa":
            print("Rekomendasi paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "kota":
        if waktu == "pagi" and tipe == "dewasa":
            print("Rekomendasi paket C")
        elif waktu == "malam":
            print("Rekomendasi paket C")
        else:
            print("Tidak ada paket yang cocok")
