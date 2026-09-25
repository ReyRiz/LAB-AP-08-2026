menu = ["Kopi Susu","Matcha Latte","Americano"]
harga = [18000,22000,15000]
jumlah = [4,3,5]

subtotal_Kopi = harga[0] * jumlah[0]
subtotal_Matcha = harga[1] * jumlah[1]
subtotal_Americano = harga[2] * jumlah[2]

subtotal_pendapatan = [subtotal_Kopi, subtotal_Matcha, subtotal_Americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print("----- Laporan Pejualan Kopi Senja -----")
print("Kopi Susu: Rp." + str(subtotal_Kopi))
print("Matcha : Rp." + str(subtotal_Matcha))
print("Amerikcano : Rp." + str(subtotal_Americano))
print("Total Pendapatan : Rp." + str(total_seluruh))
print("Pendapatan Bersih : Rp." + str(pendapatan_bersih))
print("Jumlah Barang Terjual : " + str(jumlah_barang) + " pcs")
print("Hasil Target : " + str(target_tercapai))