print('--- Rekapitulasi Transaksi Dins Store ---')
print('Ketik "0" untuk menutup toko dan mengakhiri sesi')
while True:
    print()
    jumlah = (input('Masukkan jumlah item :'))
    try: 
        item = int(jumlah)
    except:
        print('Input harus berupa angka!')
        continue
    if item < 0:
        print('Jumlah tidak boleh negatif!')
        continue
    elif item > 100:
        print('Maksimal 100 item per transaksi!')
        continue
    elif item == 0:
        print('Toko ditutup. Sesi rekap selesai.')
        break
    else:
        print(f'Transaksi {item} item berhasil')