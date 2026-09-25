#barang, harga, jumlah
minuman = ["Kopi susu", "Matcha latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#pendapatan masing-masing minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

#subtotal pendapatan dan total seluruh
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sum(subtotal_pendapatan)

#biaya operasional dan pendapatan bersih
biaya_operasional = 15000
pendapatan_bersih = total_seluruh - biaya_operasional

#minuman terjual dan target penjualan
minuman_terjual = sum(jumlah)
target = pendapatan_bersih > 200000 and minuman_terjual > 10

#keluaran
print("Subtotal pendapatan = ", subtotal_pendapatan)
print("Pendapatan bersih = ", pendapatan_bersih)
print("Target penjualan = ", target)
