#Nomor 2
jarak_pengiriman = int(input("masukkan jarak pengiriman: "))
express = input("Apakah kamu mau express? ya/tidak").lower()

if jarak_pengiriman < 5:
    harga_pengiriman = 10000
elif 5 <= jarak_pengiriman <= 20:
    harga_pengiriman = 20000
else:
    harga_pengiriman = 35000

express = harga_pengiriman + 15000 if (express == "ya") else harga_pengiriman
harga_fix = express

print(f"harga tiket yang harus di bayar:{harga_fix}")