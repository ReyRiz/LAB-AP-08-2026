'''Validasi Data Mahasiswa'''

import re

print("=== Validasi Data Mahasiswa ===")
nim   = input("Masukkan NIM      : ")
email = input("Masukkan Email    : ")
nomor = input("Masukkan No. Telp : ")

def proses_validasi(nim, email, nomor):
    print("\n--- Hasil Validasi ---")
    pattern_nim = r'^H071[0-9]{6}$'
    result_nim = re.match(pattern_nim, nim)
    pattern_email = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    result_email = re.match(pattern_email, email)
    pattern_nomor = r'^(\+62|0)8[1-9][0-9]{7,11}$'
    result_nomor = re.match(pattern_nomor, nomor)

    if result_nim:
        print("NIM         : Valid")
    else:
        print("Format NIM tidak valid!")
    if result_email:
        print("Email       : Valid")
    else:
        print("Format email tidak valid!")
    if result_nomor:
        print("No. Telepon : Valid")
    else:
        print("Nomor telepon tidak valid!")

    return (
        result_nim, result_email, result_nomor
    )

n, e, no = proses_validasi(nim, email, nomor)
if n and e and no:
    print("\nData mahasiswa berhasil diverifikasi!")