import re

def validasi_nim(nim):
    pola = r"^H071[0-9]{6}$"
    if re.match(pola, nim):
        return True
    else:
        return False

def validasi_email(email):
    pola = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(\.[a-zA-Z]+)+$"
    if re.match(pola, email):
        return True
    else:
        return False

def validasi_telepon(telepon):
    pola = r"^[0-9]{10,13}$"
    if re.match(pola, telepon):
        return True
    else:
        return False

print("=== Validasi Data Mahasiswa ===")
print()
 
nim = input("Masukkan NIM      : ").strip()
email = input("Masukkan Email    : ").strip()
telepon = input("Masukkan No. Telp : ").strip()
 
nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)
 
print()
print("--- Hasil Validasi ---")
 
if nim_valid:
    print("NIM         : Valid")
else:
    print("NIM         : Format NIM tidak valid!")
 
if email_valid:
    print("Email       : Valid")
else:
    print("Email       : Format email tidak valid!")
 
if telepon_valid:
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")
 
print()
 
if nim_valid and email_valid and telepon_valid:
    print("Data mahasiswa berhasil diverifikasi!")