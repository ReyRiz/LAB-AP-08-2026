print("=== Konversi Suhu ===")
def konversi_suhu(suhu, asal, tujuan):
    if asal != "C" and asal != "F" and asal != "K":
        raise ValueError
    if tujuan != "C" and tujuan != "F" and tujuan != "K":
        raise ValueError

    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if tujuan == "C":
        return celsius
    elif tujuan == "F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15

while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan == "selesai":
        break
    try:
        suhu = float(masukan)
    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue
    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")
    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")