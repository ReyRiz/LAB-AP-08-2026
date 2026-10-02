print("Selamat datang di Kasir Minimarket!")

def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 9 // 10
    return subtotal

while True:
    status = input("Apakah Anda member? (y/n): ")
    if status == "y" or status == "n":
        break
    print("Input tidak valid, ketik y atau n.")
member = status == "y"

total = 0
while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    try:
        int(nama_barang)
        print("Nama barang tidak boleh berupa angka.")
    except ValueError:
        harga = int(input("Harga barang: ").replace(".", ""))
        jumlah = int(input("Jumlah barang: ").replace(".", ""))
        subtotal = hitung_subtotal(harga, jumlah, adalah_member=member)
        print(f"Subtotal {nama_barang}: Rp{subtotal:,}".replace(",", "."))
        total += subtotal

print(f"Total belanja: Rp{total:,}".replace(",", "."))