'''Pembersihan Data Nomor Telepon'''

import re

print("=== Pembersihan Data Nomor Telepon ===")

jumlah = int(input("\nMasukkan jumlah data: "))
data_nomor = []
for i in range(jumlah):
    nomor = input(f"\nNomor ke-{i+1}: ")
    data_nomor.append(nomor)

def pembersihan_nomor(daftar_nomor):
    pattern = r'[\s-]'
    replace = ''

    nomor_valid = []
    for i, nomor in enumerate(daftar_nomor):
        bersih = re.sub(pattern, replace, nomor)
        print(f'Data {i+1}:')
        print(f'sebelum : {nomor}')
        print(f'sesudah : {bersih}')

        if re.match(r'^\d{10,13}', bersih):
            print(f"Status  : Valid\n")
            nomor_valid.append(bersih)
        else:
            print("Status  : Tidak valid\n")

    return nomor_valid

print("\n--- Hasil Pembersihan ---\n")
nomor_valid = pembersihan_nomor(data_nomor)
print(f"Jumlah nomor valid: {len(nomor_valid)}")