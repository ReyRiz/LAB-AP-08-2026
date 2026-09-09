harga_kopi = 18000
jumlah_kopi = 5

harga_matcha = 22000
jumlah_matcha = 3

harga_americano = 15000
jumlah_americano = 5

sub_kopi = harga_kopi * jumlah_kopi
sub_matcha = harga_matcha * jumlah_matcha
sub_americano = harga_americano * jumlah_americano

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sum(subtotal_pendapatan)

biaya_operasional = 150000
pendapatan_bersih = total_seluruh - biaya_operasional

total_barang = jumlah_kopi + jumlah_matcha + jumlah_americano
target_tercapai = total_seluruh >= 200000 and total_barang >= 10

print('subtotal pendapatan kopi:', sub_kopi)
print('subtotal pendapatan matcha:', sub_matcha)
print('subtotal pendapatan americano:', sub_americano)
print('total pendapatan:', total_seluruh)
print('pendapatan bersih:', pendapatan_bersih)
print('total barang:', total_barang)
print('target tercapai:', target_tercapai)