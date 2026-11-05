import re


# Fungsi membersihkan nomor: hapus semua spasi dan tanda minus (-)
def bersihkan_nomor(nomor):
    return re.sub(r"[\s\-]", "", nomor)


# Fungsi mengecek nomor: hanya angka, panjang 10 sampai 13 digit
def validasi_telepon(nomor):
    pola = r"^[0-9]{10,13}$"
    if re.match(pola, nomor):
        return True
    else:
        return False


print("=== Pembersihan Data Nomor Telepon ===")
print()

# Minta jumlah data sampai pengguna memasukkan angka bulat lebih dari 0
while True:
    try:
        jumlah = int(input("Masukkan jumlah data: "))
        if jumlah > 0:
            break
        print("Jumlah data harus lebih dari 0!")
    except ValueError:
        print("Masukkan angka bulat!")

data_sebelum = []
data_sesudah = []
nomor_valid = []

for i in range(1, jumlah + 1):
    print()
    nomor = input(f"Nomor ke-{i}: ")
    bersih = bersihkan_nomor(nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(bersih)

    # hanya nomor yang valid yang masuk ke list nomor_valid
    if validasi_telepon(bersih):
        nomor_valid.append(bersih)

print()
print("--- Hasil Pembersihan ---")

for i in range(len(data_sebelum)):
    print()
    print(f"Data {i + 1}:")
    print(f"{'Sebelum':<7} : {data_sebelum[i]}")
    print(f"{'Sesudah':<7} : {data_sesudah[i]}")
    if validasi_telepon(data_sesudah[i]):
        print(f"{'Status':<7} : Valid")
    else:
        print(f"{'Status':<7} : Tidak valid")

print()
print(f"Jumlah nomor valid: {len(nomor_valid)}")