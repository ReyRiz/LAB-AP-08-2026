def nilai_rekap(*nilai: float):
    rata_rata = sum(nilai) / len(nilai)
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)
    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []

while True:
    try:
        nilai_input = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if nilai_input == "":
            break
        nilai = float(nilai_input)
        daftar_nilai.append(nilai)
    except ValueError:
        print("Input harus berupa angka!")

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = nilai_rekap(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")