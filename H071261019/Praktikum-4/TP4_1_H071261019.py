
print('Selamat datang di Kasir Minimaket!\n')

def program_kasir(harga_barang, jumlah_barang, member=True):
    '''PROGRAM KASIR SEDERHANA'''
    total_harga = harga_barang * jumlah_barang
    if member:
        total_harga = total_harga * 0.9
    return int(total_harga)

total_belanja = 0

while True:
    input_member = input('Apakah Anda member? (y/n): ')
    if input_member == 'y':
        status_member = True  
        break
    elif input_member == 'n':
        status_member = False
        break
    else :
        print('Input harus y/n!\n')
        continue

while True:

    nama_barang = str(input('Masukkan nama barang (kosongkan untuk selesai): '))
    if nama_barang == '':
        break

    harga_barang = int(input('Harga barang : '))
    jumlah_barang = int(input('Jumlah barang : '))

    subtotal_barang = program_kasir(harga_barang, jumlah_barang, member = status_member)
    print(f'subtotal {nama_barang}: Rp{subtotal_barang}\n')
    total_belanja = total_belanja + subtotal_barang

print(f'total belanja: Rp{total_belanja}\n')
