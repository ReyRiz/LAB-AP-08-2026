def hitungan_mundur(detik):
    if detik == 0:
        print(detik)
        print("Luncurkan!")
    else:
        print(detik)
        hitungan_mundur(detik - 1)

while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
            continue
        break
    except ValueError:
        print("Input harus berupa angka bilangan bulat!")

hitungan_mundur(angka_awal)