def konversi_suhu(nilai, asal_suhu, tujuan_suhu):
    skala = {"C", "F", "K"}
    asal_suhu = asal_suhu.upper()
    tujuan_suhu = tujuan_suhu.upper()

    if asal_suhu not in skala or tujuan_suhu not in skala:
        raise ValueError("Skala suhu tidak dikenali.")

    # Ubah dulu ke Celsius
    if asal_suhu == "C":
        celsius = nilai
    elif asal_suhu == "F":
        celsius = (nilai - 32) * 5 / 9
    else:
        celsius = nilai - 273.15

    # Dari Celsius ke skala tujuan_suhu
    if tujuan_suhu == "C":
        return celsius
    if tujuan_suhu == "F":
        return celsius * 9 / 5 + 32
    return celsius + 273.15

print("=== Konversi Suhu ===")

while True:
    masukan_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip()
    if masukan_suhu.lower() == "selesai":
        break

    asal_suhu = input("Skala asal suhu (C/F/K): ").strip()
    tujuan_suhu = input("Skala tujuan suhu (C/F/K): ").strip()

    try:
        suhu = float(masukan_suhu)
        hasil = konversi_suhu(suhu, asal_suhu, tujuan_suhu)
        print(f"Hasil: {suhu} {asal_suhu.upper()} = {hasil:.1f} {tujuan_suhu.upper()}")
    except ValueError as error:
        if str(error) == "Skala suhu tidak dikenali.":
            print("Error: Skala suhu tidak dikenali.")
        else:
            print("Error: suhu harus berupa angka.")