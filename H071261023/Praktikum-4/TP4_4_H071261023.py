def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    if skala_asal not in ["C", "F", "K"] or skala_tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali!")

    if skala_asal == "C":
        celcius = suhu
    elif skala_asal == "F":
        celcius = (suhu - 32) * 5 / 9
    elif skala_asal == "K":
        celcius = suhu - 273

    if skala_tujuan == "C":
        hasil = celcius
    elif skala_tujuan == "F":
        hasil = (celcius * 5 / 9) + 32
    elif skala_tujuan == "K":
        hasil = celcius + 273

    return hasil

print("=== Konversi Suhu")
while True:
    input_suhu = input("Masukkan suhu: ")
    if input_suhu.lower() == "selesai":
        break
    try:
        suhu = float(input_suhu)
        skala_asal = input("Skala asal (C / F / K): ")
        skala_tujuan = input("Skala tujuan (C / F / K): ")

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")
    except ValueError as a:
        print(f"Error: {a}")
