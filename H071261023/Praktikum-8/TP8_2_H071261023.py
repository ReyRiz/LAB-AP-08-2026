print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
import re

def cek_username(username):
    if re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]{4,11}", username):
        return True
    else:
        return False

daftar_username = []
while True:
    username = input("\nMasukkan username: ")

    if username == "SELESAI".lower():
        break

    if cek_username(username):
        print("Username tersedia.")
        daftar_username.append(username)
    else:
        print("Username tidak valid!")

print("\n=== Rekapitulasi ===")
print("Username valid:")

for i in range(len(daftar_username)):
    print(str(i + 1) + ".", daftar_username[i])

print("\nJumlah username valid:", len(daftar_username))