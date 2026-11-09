import re

def bersihkan_nomor(nomor):
    hasil = re.sub(r"[ -]", "", nomor)
    return hasil
def validasi_nomor(nomor):
    hasil = re.match(r"^[0-9]{10,13}$", nomor)
    if hasil:
        return True
    else:
        return False
print("=== Pembersihan Data Nomor Telepon ===")
print("\n")
jumlah = int(input("Masukkan jumlah data: "))
data_sebelum = []
data_sesudah = []
nomor_valid = []
for i in range(jumlah):
    print("\n")
    nomor = input("Nomor ke-" + str(i + 1) + ": ")
    nomor_bersih = bersihkan_nomor(nomor)
    data_sebelum.append(nomor)
    data_sesudah.append(nomor_bersih)
    if validasi_nomor(nomor_bersih):
        nomor_valid.append(nomor_bersih)
print("\n")
print("--- Hasil Pembersihan ---")

for i in range(jumlah):
    print("\n")
    print("Data " + str(i + 1) + ":")
    print("Sebelum :", data_sebelum[i])
    print("Sesudah :", data_sesudah[i])
    if validasi_nomor(data_sesudah[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")
print("\n")
print("Jumlah nomor valid:", len(nomor_valid))