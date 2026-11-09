def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    return subtotal * 0.9 if adalah_member else subtotal

print("Selamat datang di Kasir Minimarket!")
member = input("Apakah Anda member? (y/n): ").strip().lower() == "y"
print(member)
total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ").strip()
    if not nama_barang:
        break
    while True:
        try:
            harga = int(input("Harga barang: "))
            break
        except ValueError:
            print("Harga harus berupa angka")
    while True:
        try:
            jumlah =  int(input("Jumlah barang: "))
            break
        except ValueError:
            print("Jumlah harus berupa angka")
    subtotal = hitung_subtotal(harga, jumlah, member)
    subtotal = int(subtotal)
    total += subtotal
    print(f"Subtotal {nama_barang}: Rp{subtotal}")

print(f"Total belanja: Rp{total}")
