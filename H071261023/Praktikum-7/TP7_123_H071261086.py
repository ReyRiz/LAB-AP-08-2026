import os
import random
from datetime import datetime

FOLDER_INVOICE = "invoices"
FILE_RIWAYAT = "trx_history.txt"

def buat_id_transaksi(kasir, waktu):
  
    inisial = "".join(kasir.split())[:3].upper()
    if not inisial:
        inisial = "KSR"

    bagian_waktu = waktu.strftime("%y%m%d%H%M")

    while True:
        angka_acak = random.randint(100, 999)
        id_transaksi = f"{inisial}{bagian_waktu}{angka_acak}"
        nama_file = os.path.join(FOLDER_INVOICE, f"{id_transaksi}.txt")

        if not os.path.exists(nama_file):
            return id_transaksi

def buat_transaksi():
    os.makedirs(FOLDER_INVOICE, exist_ok=True)

    kasir = input("Nama kasir: ").strip()

    waktu = datetime.now()
    id_transaksi = buat_id_transaksi(kasir, waktu)
    barang = []

    while True:
        nama = input("Nama produk (kosong untuk selesai): ").strip()

        if not nama:
            if barang:
                break
            print("Masukkan setidaknya satu produk.")
            continue

        try:
            harga = int(input("Harga produk: "))
            jumlah = int(input("Jumlah dibeli: "))

            if harga < 0 or jumlah <= 0:
                print("Harga tidak boleh negatif dan jumlah harus lebih dari 0.")
                continue

            barang.append((nama, harga, jumlah))

        except ValueError:
            print("Harga dan jumlah harus berupa angka.")

    total = sum(harga * jumlah for _, harga, jumlah in barang)

    isi_invoice = (
        f"ID transaksi: {id_transaksi}\n"
        f"Kasir: {kasir}\n"
        f"Waktu: {waktu:%d-%m-%Y %H:%M}\n"
        + "-" * 40 + "\n"
    )

    for nama, harga, jumlah in barang:
        subtotal = harga * jumlah
        isi_invoice += (
            f"{nama} x{jumlah} @Rp{harga:,} = Rp{subtotal:,}\n"
        )

    isi_invoice += "+" * 40 + f"\nTOTAL: Rp{total:,}"

    nama_file_invoice = os.path.join(
        FOLDER_INVOICE, f"{id_transaksi}.txt"
    )

    with open(nama_file_invoice, "w", encoding="utf-8") as file:
        file.write(isi_invoice)

    catat_riwayat(waktu, id_transaksi, total)

    print("\n" + isi_invoice)
    print(f"\nInvoice disimpan di: {nama_file_invoice}")


def cari_invoice():
    os.makedirs(FOLDER_INVOICE, exist_ok=True)

    id_cari = input("Masukkan ID transaksi: ").strip()
    nama_file = os.path.join(FOLDER_INVOICE, id_cari + ".txt")

    if os.path.isfile(nama_file):
        with open(nama_file, "r", encoding="utf-8") as file:
            print("\n" + file.read())
    else:
        print("Invoice tidak ditemukan.")

def catat_riwayat(waktu, id_transaksi, nominal):
    file_baru = not os.path.exists(FILE_RIWAYAT)

    with open(FILE_RIWAYAT, "a", encoding="utf-8") as file:
        if file_baru:
            file.write(
                f"{'Waktu':<19} | "
                f"{'ID Transaksi':<18} | "
                f"Nominal Transaksi\n"
            )
            file.write("-" * 68 + "\n")

        file.write(
            f"{waktu:%Y-%m-%d %H:%M:%S} | "
            f"{id_transaksi:<18} | "
            f"Rp. {nominal}\n"
        )

while True:
    print("\n=== APLIKASI KASIR ===")
    print("1. Buat transaksi dan invoice")
    print("2. Cari invoice")
    print("3. Keluar")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        buat_transaksi()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
