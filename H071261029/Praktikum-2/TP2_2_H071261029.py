# Menghitung tarif pengiriman barang berdasarkan jarak

jarak = float(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ")

# if jarak < 0:
#     print("Input Tidak Valid")
if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
elif jarak >= 20:
    tarif = 35000
else:
    print("Input Tidak Valid")

tarif_tambahan = 15000 if express == "ya" else 0 
total_tarif = tarif + tarif_tambahan
print(f"Total tarif pengiriman: {total_tarif}")
