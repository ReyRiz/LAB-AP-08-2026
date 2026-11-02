def kasir(harga, jumlah, member=False):
    subtotal = harga * jumlah
    if member:
        subtotal = subtotal * 0.90
    return int(subtotal)

print("\nSelamat datang di minimarket")

status_member = input("Apakah Anda member? (y/n): ")
member = status_member == "y"

total = 0

while True:
    nama_barang = input("Masukkan nama barang: ")
    if nama_barang == "":
        print("Sesi selesai, terima kasih")
        break
    harga_barang = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = kasir(harga_barang, jumlah, member)
    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total += subtotal
    print(f"Total belanja: Rp{total}")
