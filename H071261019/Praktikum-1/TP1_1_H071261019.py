menu = ['Kopi susu', 'Macha latte', 'Americano']
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = jumlah[0] * harga[0]
sub_macha = jumlah[1] * harga[1]
sub_americano = jumlah[2] * harga[2]
subtotal_pendapatan = (sub_kopi, sub_macha, sub_americano)

total_seluruh = sum(subtotal_pendapatan)

biaya_operasional = 15000
pendapatan_bersih = total_seluruh - biaya_operasional
jumlah_barang = sum(jumlah)
#print(jumlah_barang)

print('subtotal penjualan adalah Rp.', total_seluruh,
       'dan pendapatan bersihnya adalah Rp.', pendapatan_bersih)

if pendapatan_bersih > 200000 and jumlah_barang > 10:
    print('hasil target tercapai')
else:
    print('hasil target tidak tercapai')
    

