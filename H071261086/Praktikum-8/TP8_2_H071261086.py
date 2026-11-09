import re

def validasi_username(username):
    pola = r'^[A-Za-z][A-Za-z0-9_]{4,11}$'
    return re.match(pola, username)

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print()

daftar_valid = []

while True:
    username = input("Masukkan username: ")
    
    if username == "SELESAI":
        break
    
    if validasi_username(username):
        print("Username tersedia.")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!")
    
    print()

print("=== Rekapitulasi ===")
print("Username valid:")
for i, user in enumerate(daftar_valid, start=1):
    print(f"{i}. {user}")

print()
print(f"Jumlah username valid: {len(daftar_valid)}")
