def hitung_mundur(angka):
    if angka == 0:
        print(0)
        print("Luncurkan!")
        return
    print(angka)
    hitung_mundur(angka - 1)

angka_awal = int(input("Masukkan angka awal hitung mundur: "))
if angka_awal < 0:
    print("Angka tidak boleh negatif!")
else:
    hitung_mundur(angka_awal)
