import os
import random
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_INVOICE = os.path.join(BASE_DIR, "invoices")
FILE_RIWAYAT = os.path.join(BASE_DIR, "trx_history.txt")

# Lebar kolom tabel riwayat
LEBAR_WAKTU = 19
LEBAR_ID = 25
LEBAR_NOMINAL = 20
LEBAR_TABEL = LEBAR_WAKTU + LEBAR_ID + LEBAR_NOMINAL + 10

def buat_id_transaksi(nama_kasir, sekarang):
    """ID = inisial kasir (kapital) + yy + mm + dd + HHMM + 3 digit acak."""
    inisial = "".join(kata[0].upper() for kata in nama_kasir.split() if kata[0])
    tanggal_waktu = sekarang.strftime("%y%m%d%H%M")
    angka_acak = random.randint(100, 999)
    return f"{inisial}{tanggal_waktu}{angka_acak}"

def buat_id_unik(nama_kasir, sekarang):
    """Memastikan ID belum dipakai agar invoice lama tidak tertimpa."""
    while True:
        id_transaksi = buat_id_transaksi(nama_kasir, sekarang)
        if not os.path.exists(os.path.join(FOLDER_INVOICE, f"{id_transaksi}.txt")):
            return id_transaksi

# riwayat transaksi (nomor 3)
def catat_riwayat(waktu, id_transaksi, total_belanja):
    file_kosong = (not os.path.exists(FILE_RIWAYAT)) or os.path.getsize(FILE_RIWAYAT) == 0

    with open(FILE_RIWAYAT, "a", encoding="utf-8") as file:
        if file_kosong:
            file.write("=" * LEBAR_TABEL + "\n")
            file.write(
                f"| {'Waktu':^{LEBAR_WAKTU}} | {'ID Transaksi':^{LEBAR_ID}} "
                f"| {'Nominal Transaksi':^{LEBAR_NOMINAL}} |\n"
            )
            file.write("=" * LEBAR_TABEL + "\n")

        nominal_teks = f"Rp. {total_belanja}"
        file.write(
            f"| {waktu:^{LEBAR_WAKTU}} | {id_transaksi:<{LEBAR_ID}} "
            f"| {nominal_teks:<{LEBAR_NOMINAL}} |\n"
        )
        file.write("=" * LEBAR_TABEL + "\n")

# membuat invoice (nomor 1)
def buat_invoice(nama_kasir, daftar_barang):
    if len(daftar_barang) == 0:
        print("Tidak ada barang yang dibeli.")
        return

    os.makedirs(FOLDER_INVOICE, exist_ok=True)

    # satu waktu dipakai untuk ID, invoice, dan riwayat agar konsisten
    sekarang = datetime.now()
    waktu_lengkap = sekarang.strftime("%Y-%m-%d %H:%M:%S")
    id_transaksi = buat_id_unik(nama_kasir, sekarang)
    nama_file = os.path.join(FOLDER_INVOICE, f"{id_transaksi}.txt")

    total_belanja = sum(barang["subtotal"] for barang in daftar_barang)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"{'=' * 50}\n")
        file.write(f"{'TOKO SERBA ADA':^50}\n")
        file.write(f"{'=' * 50}\n")
        file.write(f"ID TRANSAKSI : {id_transaksi}\n")
        file.write(f"Waktu        : {waktu_lengkap}\n")
        file.write(f"Kasir        : {nama_kasir}\n")
        file.write(f"{'-' * 50}\n")
        file.write(f"{'Nama Produk':<20}{'Harga':<10}{'Jumlah':<8}{'Subtotal'}\n")
        file.write(f"{'-' * 50}\n")

        for barang in daftar_barang:
            nama_produk = barang["nama"][:18]  # dipotong agar kolom tetap rapi
            file.write(
                f"{nama_produk:<20}{barang['harga']:<10}{barang['jumlah']:<8}{barang['subtotal']}\n"
            )

        file.write(f"{'-' * 50}\n")
        file.write(f"TOTAL AKHIR  : Rp. {total_belanja}\n")
        file.write(f"{'=' * 50}\n")
        file.write(f"{'Terima Kasih Telah Berbelanja!':^50}\n")
        file.write(f"{'=' * 50}\n")

    catat_riwayat(waktu_lengkap, id_transaksi, total_belanja)

    print(f"\nTransaksi berhasil! ID Transaksi : {id_transaksi}")
    print(f"File invoice tersimpan di : {os.path.abspath(nama_file)}")
    print(f"Riwayat transaksi di      : {os.path.abspath(FILE_RIWAYAT)}")


# cari invoice (nomor 2)
def cari_invoice(id_transaksi):
    # basename mencegah input seperti "../file" keluar dari folder invoices
    id_bersih = os.path.basename(id_transaksi.strip())
    if id_bersih.lower().endswith(".txt"):
        id_bersih = id_bersih[:-4]

    kandidat = [
        os.path.join(FOLDER_INVOICE, f"{id_bersih}.txt"),
        os.path.join(FOLDER_INVOICE, f"{id_bersih.upper()}.txt"),
    ]
    nama_file = next((f for f in kandidat if os.path.isfile(f)), None)

    if nama_file is None:
        print(f"\n>> Error: File invoice dengan ID '{id_transaksi}' tidak ditemukan di komputer!")
        return

    print("\n" + "=" * 50)
    print(f"{'HASIL PENCARIAN INVOICE':^50}")
    print("=" * 50)

    with open(nama_file, "r", encoding="utf-8") as file:
        print(file.read())


def input_transaksi():
    print(f"\n{'-' * 45}")
    print(f"{'INPUT TRANSAKSI BARU':^45}")
    print(f"{'-' * 45}\n")

    nama_kasir = input("Masukkan nama kasir: ").strip()
    if not any(c.isalnum() for c in nama_kasir):
        print("\n>> Error: Nama kasir tidak boleh kosong!\n")
        return

    daftar_barang = []

    while True:
        nama_produk = input("\nNama produk (tekan Enter jika selesai): ").strip()
        if len(nama_produk) == 0:
            break

        try:
            harga = int(input(f"Harga '{nama_produk}': Rp. "))
            jumlah = int(input(f"Jumlah beli '{nama_produk}': "))
        except ValueError:
            print("\n>> Error: Masukan harga dan jumlah harus berupa angka bulat!\n")
            continue

        if harga <= 0 or jumlah <= 0:
            print("\n>> Error: Harga dan jumlah harus berupa angka positif!\n")
            continue

        daftar_barang.append(
            {
                "nama": nama_produk,
                "harga": harga,
                "jumlah": jumlah,
                "subtotal": harga * jumlah,
            }
        )
        print(f"\n>> Berhasil menambahkan: {nama_produk} x {jumlah}")

    if len(daftar_barang) == 0:
        print("\n>> Transaksi dibatalkan karena tidak ada barang yang diinput.\n")
    else:
        buat_invoice(nama_kasir, daftar_barang)


def main():
    while True:
        print(f"\n{'=' * 45}")
        print(f"{'APLIKASI KASIR - TOKO SERBA ADA':^45}")
        print(f"{'=' * 45}")
        print("1. Transaksi Baru")
        print("2. Cari Invoice")
        print("3. Keluar")
        print(f"{'-' * 45}\n")

        pilihan = input("Pilih Menu (1-3): ").strip()

        if pilihan == "1":
            input_transaksi()
        elif pilihan == "2":
            print(f"\n{'-' * 45}")
            print(f"{'PENCARIAN INVOICE':^45}")
            print(f"{'-' * 45}\n")
            id_dicari = input("Masukkan ID Transaksi: ").strip()
            if not id_dicari:
                print("\n>> Error: ID Transaksi tidak boleh kosong!\n")
            else:
                cari_invoice(id_dicari)
        elif pilihan == "3":
            print(f"\n{'-' * 45}")
            print(f"{'Terima kasih telah menggunakan sistem kasir!':^45}")
            print(f"{'-' * 45}\n")
            break
        else:
            print("\n>> Pilihan tidak valid, silahkan ketik angka 1, 2, atau 3.\n")


if __name__ == "__main__":
    main()