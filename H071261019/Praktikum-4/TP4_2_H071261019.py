def nilai_ujian(*nilai):
    '''Menghitung semua nilai'''
    rata_rata = sum(nilai) / len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    masukan_nilai = input('Masukkan nilai ujian siswa (kosongkan untuk selesai): ')
    if masukan_nilai == '':
        break
    daftar_nilai.append(int(masukan_nilai))
    
if not daftar_nilai:
    print('Data tidak tersedia')
else:
    rata_rata, tertinggi, terendah = nilai_ujian(*daftar_nilai)
    
    print(f'Rata-rata kelas: {rata_rata}')
    print(f'Nilai tertinggi: {tertinggi}')
    print(f'Nilai terendah: {terendah}')