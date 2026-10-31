''' Sistem Penyaringan Username'''

import re

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

list_username = []
def validasi_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.]\w{4,11}$'
    result = re.match(pattern, username)
    if result:
        print("Username tersedia.\n")
        list_username.append(username)
    else:
        print("Username tidak valid!\n")

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI":
        break
    validasi_username(username)

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, username in enumerate(list_username, start=1):
    print(f"{i}. {username}")
print(f"\nJumlah username valid: {len(list_username)}")
