print ("=== Validasi Data Mahasiswa===\n")
nim = input("Masukkan NIM            : ")
email = input("Masukkan email          : ")
telepon = input("Masukkan nomor telepon  : ")
import re

def cek_nim(nim):
    if re.fullmatch(r"H071\d{6}", nim):
        print("NIM           :valid")
        return True
    else:
        print("Format NIM    :tidak valid!")
        return False

def cek_email(email):
    if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}", email):
        print("Email         :valid")
        return True
    else:
        print("Format email  :tidak valid!")
        return False
    
def cek_telepon(telepon):
    if re.fullmatch(r"\d{10,13}", telepon):
        print("Nomor telepon :valid")
        return True
    else:
        print("Nomor telepon :tidak valid!")
        return False

print ("\n=== Hasil Validasi ===")
hasil_nim = cek_nim(nim)
hasil_email = cek_email(email)
hasil_telepon = cek_telepon(telepon)

if hasil_nim and hasil_email and hasil_telepon:
    print("\nData mahasiswa berhasil diverifikasi!")
