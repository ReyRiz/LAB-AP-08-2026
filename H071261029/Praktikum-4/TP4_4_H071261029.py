def konversi_suhu(suhu: float, asal: str, tujuan: str):
    skala_valid = ["C", "F", "K"]

    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali")

    if asal == "C":
        if tujuan == "F":
            return (suhu * 1.8) + 32
        elif tujuan == "K":
            return suhu + 273.15
        else:
            return suhu
    elif asal == "F":
        if tujuan == "C":
            return (suhu - 32) * 5 / 9
        elif tujuan == "K":
            return (suhu - 32) * 5 / 9 + 273.15
        else:
            return suhu
    elif asal == "K":
        if tujuan == "C":
            return suhu - 273.15
        elif tujuan == "F":
            return (suhu - 273.15) * 1.8 + 32
        else:
            return suhu

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu == "selesai":
        break

    try:
        suhu = float(input_suhu)
        skala_asal = input("Skala asal (C/F/K): ")
        skala_tujuan = input("Skala tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")

    except:
        print("Error: Skala suhu tidak dikenali.")