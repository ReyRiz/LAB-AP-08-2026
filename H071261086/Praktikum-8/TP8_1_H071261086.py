import re

def validasi_nim(nim):
    return re.fullmatch(r'H071\d{6}', nim)

def validasi_email(email):
    return re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email)

def validasi_telepon(telepon):
    return re.fullmatch(r'\d{10,13}', telepon)


print("=== Validasi Data Mahasiswa ===\n")

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print("\n--- Hasil Validasi ---")

nim_valid = bool(validasi_nim(nim))
email_valid = bool(validasi_email(email))
telepon_valid = bool(validasi_telepon(telepon))

if nim_valid:
    print("NIM         : Valid")
else:
    print("Format NIM tidak valid!")

if email_valid:
    print("Email       : Valid")
else:
    print("Format email tidak valid!")

if telepon_valid:
    print("No. Telepon : Valid")
else:
    print("Nomor telepon tidak valid!")

print()
if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")
