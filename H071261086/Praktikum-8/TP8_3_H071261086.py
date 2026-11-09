import re

def bersihkan_nomor(nomor):
    return re.sub(r'[\s-]', '', nomor)

def validasi_nomor(nomor_bersih):
    pola = r'^\d{10,13}$'
    return re.match(pola, nomor_bersih)

print("--- Pembersihan Data Nomor Telepon ---")
print()

jumlah = int(input("Masukkan jumlah data: "))
print()

data_sebelum = []
data_sesudah = []
list_status = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"Nomor ke-{i}: ")
    data_sebelum.append(nomor)
    
    bersih = bersihkan_nomor(nomor)
    data_sesudah.append(bersih)
    
    if validasi_nomor(bersih):
        list_status.append("Valid")
        nomor_valid.append(bersih)
    else:
        list_status.append("Tidak valid")
    print()

print("--- Hasil Pembersihan ---")
print()
for i in range(jumlah):
    print(f"Data {i+1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")
    print(f"Status  : {list_status[i]}")

    print()

print(f"Jumlah nomor valid: {len(nomor_valid)}")
