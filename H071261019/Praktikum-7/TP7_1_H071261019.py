'''Membuat Invoice dari Transaksi'''

import os
import random
from datetime import datetime

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder_saat_ini, "invoices")
file_history = os.path.join(folder_saat_ini, "trx_history.txt")
os.makedirs(folder_invoices, exist_ok=True)

def membuat_file(kasir):

    inisial = "".join([huruf[0].upper() for huruf in kasir.split()])
    sekarang = datetime.now()
    tahun = sekarang.strftime("%y")
    bulan = sekarang.strftime("%m")
    tanggal = sekarang.strftime("%d")
    waktu = sekarang.strftime("%H%M")
    angka_acak = str(random.randint(100,999))

    id_transaksi = f"{inisial}{tahun}{bulan}{tanggal}{waktu}{angka_acak}"
    return id_transaksi

def membuat_invoice():
    daftar_produk = []
    total_belanja = 0
    while True:
        nama_produk   = input("Masukkan Nama Produk      : ")
        harga_produk  = int(input("Masukkan Harga Produk     : "))
        jumlah_produk = int(input("Masukkan Jumlah Produk    : "))
        
        total_harga = harga_produk * jumlah_produk
        total_belanja += total_harga
        
        daftar_produk.append(
            {
                "nama": nama_produk,
                "harga": harga_produk,
                "jumlah": jumlah_produk,
                "total": total_harga,
            }
        )
        print("=" * 50)
        lanjut = input("Tambah produk lain? (y/t) : ")
        if lanjut.lower() != "y":
            break
        print("=" * 50)
    return total_belanja, daftar_produk

def main():
    print("=" * 50)
    print("SELAMAT DATANG".center(50))
    print("=" * 50)
    kasir = input("Masukkan nama kasir       : ")
    while True:
        
        print("=" * 50)
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. keluar")
        print("=" * 50)
        pilihan = input("Masukkan opsi pilihan     : ")
        print("=" * 50)

        if pilihan == "1":
            id_transaksi = membuat_file(kasir)
            nama_file = os.path.join(folder_invoices, f"{id_transaksi}.txt")
            total_belanja, daftar_produk = membuat_invoice()

            print("=" * 50)
            print("TRANSAKSI BERHASIL".center(50))
            with open(nama_file, "w") as file:
                file.write("=" *65 + "\n")
                file.write("PT MENCARI CINTA SEJATI".center(65) + "\n")
                file.write("=" *65 + "\n")
                file.write(f"ID Transaksi    : {id_transaksi}\n")
                file.write(f"Kasir           : {kasir}\n")
                file.write(f"Waktu Transaksi : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("-" *65 + "\n")
                file.write(f"| {'Produk':<25} | {'Harga':<10} | {'Jumlah':<6} | {'Total':<11} |\n")
                file.write("-" *65 + "\n")

                for item in daftar_produk:
                    harga_format = f'{item['harga']:,}'.replace(",",".")
                    total_format = f'{item['total']:,}'.replace(",",".")
                    file.write(
                        f"| {item['nama']:<25} | {harga_format:<10} | {item['jumlah']:<6} | {total_format:<11} |\n"
                    )

                file.write("-" *65 + "\n")
                file.write(f"Total Bayar     : Rp {total_belanja:,}\n".replace(",","."))
                file.write("=" *65 + "\n")
                file.write("Terima Kasih Atas Kunjungan Anda".center(65))
                file.write("\n" + "=" *65 + "\n")

            waktu_sekarang = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(file_history, "a") as history:
                history.write("=" *63 + "\n")
                history.write(f"| {'Tanggal':^19} | {"ID Transaksi":^17} | {'Nominal Transaksi':^17} |\n")
                history.write("=" *63 + "\n")
                nominal_format = f"{total_belanja:,}".replace(",",".")
                history.write(f"| {waktu_sekarang:^19} | {id_transaksi:^17} | {nominal_format:^17} |\n")
                history.write("=" *63 + "\n")

        elif pilihan == "2":
            id_transaksi = input("Masukkan ID transaksi: ")
            lokasi_file_folder = os.path.join(folder_invoices, id_transaksi+".txt")
            if os.path.isfile(lokasi_file_folder):
                print()
                with open(lokasi_file_folder, "r") as ada:
                    print(ada.read())
            else:
                print(f"File '{id_transaksi}' ga ada jirr.")

        elif pilihan == "3":
            print("Hati-hati di jalan. Tetap semangat <3".center(50))
            print("=" * 50)
            break
main()