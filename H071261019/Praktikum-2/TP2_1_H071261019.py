# persentase_cabai = float(input("Masukkan persentase cabai : "))
# if persentase_cabai >= 0 and persentase_cabai <= 10:
#     print("Level Aman")
# elif persentase_cabai >= 11 and persentase_cabai <= 40:
#     print("Level Sedang")
# elif persentase_cabai >= 41 and persentase_cabai <= 70:
#     print("Level Pedas")
# elif persentase_cabai >= 70:
#     print("Level Ekstem")
# else:
#     print("input tidak valid")

jarak_pengiriman = float(input("Masukkan jarak pengiriman (km) : "))
layanan_express = str(input("Layanan express (ya/tidak) : "))
biaya_pengiriman = [10000, 20000, 35000]
biaya_express = 15000
total_tarif = [i + biaya_express for i in biaya_pengiriman] if layanan_express == "ya" else biaya_pengiriman
if jarak_pengiriman < 5:
    if layanan_express == "ya":
        print("Total tarif pengiriman : Rp",total_tarif[0])
    else:
        print("Total tarif pengiriman : Rp",total_tarif[0])
elif jarak_pengiriman >= 5 and jarak_pengiriman <= 20:
    if layanan_express == "ya":
        print("Total tarif pengiriman : Rp",total_tarif[1])
    else:
        print("Total tarif pengiriman : Rp",total_tarif[1])
elif jarak_pengiriman > 20:
    if layanan_express == "ya":
        print("Total tarif pengiriman : Rp",total_tarif[2])
    else:
        print("Total tarif pengiriman : Rp",total_tarif[2])
else:
    print("input tidak valid")

# nilai = int(input("Masukkan nilai tes : "))
# pengalaman = int(input("Masukkan pengalaman kerja (tahun) : "))
# if nilai >= 80:
#     print("Lolos ke Tahap Wawancara")
# elif 65 <= nilai <= 80 and pengalaman >= 2:
#     print("Lolos Bersyarat")
# else:
#     print("Tidak Lolos")

# tujuan = str(input("Masukkan tujuan (Pantai/Pegunungan/Kota) : "))
# waktu = str(input("Masukkan waktu (Pagi/Malam) : "))
# pengunjung = str(input("Masukkan tipe pengunjung (Anak/Dewasa) : "))
# match tujuan:
#     case "Pantai":
#         if waktu == "Pagi":
#             print("Paket Rekomendasi: Paket A")
#         elif waktu == "Malam" and pengunjung == "Dewasa":
#             print("Paket Rekomendasi: Paket C")
#         else:
#             print("Tidak ada paket yang cocok")
#     case "Pegunungan":
#         if waktu == "Pagi" and pengunjung == "Dewasa":
#             print("Paket Rekomendasi: Paket B")
#         elif waktu == "Malam" and pengunjung == "Dewasa":
#             print("Paket Rekomendasi: Paket C")
#         else:
#             print("Tidak ada paket yang cocok")
#     case "Kota":
#         if waktu == "Malam":
#             print("Paket Rekomendasi: Paket C")
#         else:
#             print("Tidak ada paket yang cocok")  
#     case _ :
#         print("Tidak ada paket yang cocok")