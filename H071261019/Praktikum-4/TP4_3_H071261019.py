def hitung(n):
    '''hitung mundur sederhana'''
    if n < 0:
        return
    print(n)
    hitung(n-1)

while True:

    angka_awal = int(input('Masukkan angka awal hitung mundur: '))
    if angka_awal < 0: 
        print('Input tidak valid, angka tidak boleh negatif.')
        continue
    hitung(angka_awal)
    break

print('Luncurkan!')