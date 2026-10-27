import os
import random
from datetime import datetime

if not os.path.exists("invoices"):
    os.mkdir("invoices")

print("=" * 70)
print(" " * 30 + "SELAMAT DATANG")
print("=" * 70)
nama_kasir = input("Masukkan nama kasir    : ")

def transaksi_baru(nama_kasir):
    waktu = datetime.now()

    inisial = ""
    nama = nama_kasir.split()
    for kata in nama:
        inisial = inisial + kata[0]
    inisial = inisial.upper()

    tahun = str(waktu.year % 100)
    bulan = str(waktu.month)
    hari = str(waktu.day)
    jam = str(waktu.hour)
    menit = str(waktu.minute)

    data = [tahun, bulan, hari, jam, menit]

    for i in range(len(data)):
        if len(data[i]) == 1:
            data[i] = "0" + data[i]

    tanggal_id = tahun + bulan + hari + jam + menit
    angka_acak = str(random.randint(100, 999))
    
    id_transaksi = inisial + tanggal_id + angka_acak

    daftar_produk = []
    total = 0
    while True:
        print("=" * 70)
        nama_produk = input("Masukkan nama produk    : ")
        harga = int(input("Masukkan harga produk   : "))
        jumlah = int(input("Masukkan jumlah produk  : "))
        subtotal = harga * jumlah

        produk = [nama_produk, harga, jumlah, subtotal]
        daftar_produk.append(produk)
        total = total + subtotal

        print("=" * 70)
        tambah = input("Tambah produk? (y/t)    : ")
        if tambah.lower() == "t":
            break

    tahun_lengkap = str(waktu.year)
    waktu_invoice = ( hari + "/" + bulan + "/" + tahun + " " + jam + ":" + menit)

    invoice = ""
    invoice += "\n" 
    invoice += " " * 31 + "TOKO " + nama_kasir.upper() + "\n\n" 
    invoice += "=" * 70 + "\n" 
    invoice += "Nama kasir : " + nama_kasir + "\n"
    invoice += "Waktu transaksi : " + waktu_invoice + "\n"

    invoice += "=" * 70 + "\n\n" 
    invoice += " " * 30 + "Daftar Produk\n\n" 
    invoice += " " + "=" * 62 + "\n"

    invoice += " | {:<16} | {:>8} | {:>6} | {:>10} |\n".format(
        "Nama", "Harga", "Jumlah", "Total")
    invoice += " " + "=" * 62 + "\n"

    for produk in daftar_produk:
        nama_produk = produk[0]
        harga = produk[1]
        jumlah = produk[2]
        subtotal = produk[3]
        if len(nama_produk) > 16:
            nama_produk = nama_produk[:13] + "..."
        invoice += " | {:<16} | Rp{:>6} | {:>6} | Rp{:>8} |\n".format(
            nama_produk, harga, jumlah, subtotal
        )

    invoice += " " + "=" * 62 + "\n"
    invoice += " | {:<39} | Rp{:>8} |\n".format(
        "TOTAL", total
    )
    invoice += " " + "=" * 62 + "\n\n"
    invoice += "=" * 70 + "\n"
    invoice += " " * 23 + "TERIMA KASIH TELAH BERBELANJA\n"

    nama_file = "invoices/" + id_transaksi + ".txt"
    file = open(nama_file, "w")
    file.write(invoice)
    file.close()

    nama_history = "trx_history.txt"
    file = open(nama_history, "a")
    file.close()
    file = open(nama_history, "r")
    isi_history = file.read()
    file.close()

    if isi_history == "":
        file = open(nama_history, "a")
        file.write("=" * 70 + "\n")
        file.write("|        Waktu        |   ID Transaksi    | Nominal Transaksi    |\n")
        file.write("=" * 70 + "\n")
        file.close()

    detik = str(waktu.second)
    if len(detik) == 1:
        detik = "0" + detik
    waktu_history = (
        tahun_lengkap + "-" + bulan + "-" + hari
        + " " + jam + ":" + menit + ":" + detik
    )
    file = open(nama_history, "a")
    baris = "| " + waktu_history + " | "
    baris = baris + id_transaksi + " | Rp. " + str(total) + "\n"
    file.write(baris)
    file.write("=" * 70 + "\n")
    file.close()

    print("=" * 70)
    print(" " * 28 + "TRANSAKSI BERHASIL")
    print("=" * 70)

def cari_transaksi():
    id_transaksi = input("Masukkan ID transaksi : ")
    nama_file = "invoices/" + id_transaksi + ".txt"

    if os.path.exists(nama_file):
        file = open(nama_file, "r")
        isi_invoice = file.read()
        file.close()
        print(isi_invoice)
    else:
        print("Transaksi tidak ditemukan!")

while True:
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 70)
    pilihan = input("Masukkan opsi pilihan  : ")

    if pilihan == "1":
        transaksi_baru(nama_kasir)
    elif pilihan == "2":
        cari_transaksi()
    elif pilihan == "3":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia!")