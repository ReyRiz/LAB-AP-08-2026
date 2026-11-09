
while True:
    try:
        kursi = int(input('Masukkan maksimal kursi bus:'))
        break
    except:
        print('Input jumlah kursi harus berupa angka!')

print('--- Sistem Reservasi PO BUS Dimulai ---')  
print()
sisa_kursi = kursi
total_pendapatan = 0

while sisa_kursi > 0:
    
    print('Sisa kursi:',sisa_kursi)
    try:
        umur = int(input('Masukkan umur penumpang:'))
    except:
        print('Input umur penumpang harus berupa angka!')
        continue

    if umur < 0:
        print('Umur tidak valid!')
        continue
    elif umur <= 5:
        kategori = 'Balita'
        harga = 0
    elif umur <= 12:
        kategori = 'Anak'
        harga = 50000
    else:
        kategori = 'Dewasa'
        harga = 100000
        
    print(f"Kategori: {kategori} - Tiket Rp {harga:,}".replace(",","."))
    total_pendapatan += harga
    sisa_kursi -= 1
        
    
print('--- Semua Kursi Terisi ---')
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,}".replace(",","."))
