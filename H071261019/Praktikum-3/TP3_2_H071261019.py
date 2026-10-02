print('--- Setup Denah Biosop NontonYuk ---')

while True:
    try:
        baris = int(input('Masukkan jumlah baris: '))
    except:
        print('Input baris harus berupa angka!\n')
        
        continue
    if baris < 0:
        print('Jumlah baris harus lebih dari 0!\n')
        
        continue
    break

while True:
    try:
        kursi = int(input('Masukkan jumlah kursi per baris: '))
    except:
        print('Input kursi harus berupa angka!')
        continue
    if kursi < 0:
        print('Jumlah kursi harus lebih dari 0!')
        continue
    
    print('\n--- Daftar Kursi Tersedia---')
    for b in range(1, baris + 1):
        for k in range(1, kursi + 1):
            if k == 13:
                continue
            elif b == 1 and (k % 2) == 0:
                continue
            print(f'baris {b} - kursi {k}')
    break




                
