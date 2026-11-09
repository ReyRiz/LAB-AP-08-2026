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
