import re

def validasi_username(username):
    pola = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    if re.match(pola, username):
        return True
    else:
        return False

daftar_valid = []
 
print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
 
while True:
    print()
    username = input("Masukkan username: ").strip()
 
    if username.upper() == "SELESAI":
        break
 
    if validasi_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")
 
print()
print("=== Rekapitulasi ===")
print("Username valid:")
 
nomor = 1
for nama in daftar_valid:
    print(f"{nomor}. {nama}")
    nomor = nomor + 1
 
print()
print(f"Jumlah username valid: {len(daftar_valid)}")