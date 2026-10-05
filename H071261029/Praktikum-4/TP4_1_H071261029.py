def subtotal(harga: int, jumlah: int, /, *, adalah_member=False) -> int:
    hasil = harga * jumlah
    if adalah_member == "y":
        return hasil * 0.9
    return hasil

print("Selamat datang di Kasir Minimarket!")
status_member = str(input("Apakah Anda member? (y/n): "))

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        print(f"Total belanja: Rp{total_belanja}")
        break

    harga_barang = int(input("Harga barang: "))
    jumlah_barang = int(input("Jumlah barang: "))

    sub = int(subtotal(harga_barang, jumlah_barang, adalah_member=status_member))
    total_belanja += sub
    
    print(f"Subtotal {nama_barang}: Rp{sub}")