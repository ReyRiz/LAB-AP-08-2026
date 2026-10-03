jarak = int(input("Masukkan jarak pengiriman: "))
express = input("Layanan ekspress (ya/tidak): ")

if jarak < 5:
    harga = 10000
elif jarak >= 5 and jarak <= 20:
    harga = 20000
elif jarak > 20:
    harga = 35000

harga_express = 15000 if express == "ya" else 0
total_tarif = harga + harga_express

print("Total tarif pengiriman: ", total_tarif)

