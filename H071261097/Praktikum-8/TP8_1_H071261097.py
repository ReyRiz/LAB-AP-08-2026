import re

def validasi_nim(nim):
    hasil = re.match(r"^H071[0-9]{6}$", nim)
    if hasil:
        return True
    else:
        return False
def validasi_email(email):
    hasil = re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$", email)
    if hasil:
        return True
    else:
        return False
def validasi_telepon(telp):
    hasil = re.match(r"^[0-9]{10,13}$", telp)
    if hasil:
        return True
    else:
        return False
print("=== Validasi Data Mahasiswa ===")
print()
nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telp = input("Masukkan No. Telp   : ")
nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telp_valid = validasi_telepon(telp)
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
if telp_valid:
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Nomor telepon tidak valid!")
print()
if nim_valid and email_valid and telp_valid:
    print("Data mahasiswa berhasil diverifikasi!")
else:
    print("Data mahasiswa belum valid, periksa kembali input.")