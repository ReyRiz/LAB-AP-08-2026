import re

def validasi_username(username):
    hasil = re.match(r"^[A-Za-z][A-Za-z0-9_]{4,11}$", username)
    if hasil:
        return True
    else:
        return False

daftar_valid = []
print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
print("\n")
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
print("\n")
print("=== Rekapitulasi ===")
print("Username valid:")
nomor = 1
for nama in daftar_valid:
    print(str(nomor) + ". " + nama)
    nomor = nomor + 1
print()
print("Jumlah username valid:", len(daftar_valid))