import re

print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))

data_awal = []
data_bersih = []
nomor_valid = []

for i in range(jumlah):
    nomor = input("Nomor ke-" + str(i + 1) + ": ")
    data_awal.append(nomor)

    bersih = re.sub(r"[ -]", "", nomor)
    data_bersih.append(bersih)

    if re.fullmatch(r"\d{10,13}", bersih):
        nomor_valid.append(bersih)

print("\n--- Hasil Pembersihan ---")

for i in range(jumlah):
    print("\nData", str(i + 1) + ":")
    print("Sebelum :", data_awal[i])
    print("Sesudah :", data_bersih[i])

    if re.fullmatch(r"\d{10,13}", data_bersih[i]):
        print("Status  : Valid")
    else:
        print("Status  : Tidak valid")

print("\nJumlah nomor valid:", len(nomor_valid))