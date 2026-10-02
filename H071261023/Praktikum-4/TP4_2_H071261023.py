def rekap_nilai_ujian(*nilai):
    total = 0
    banyak = 0
    for n in nilai:
        total = total + n
        banyak = banyak + 1
    rata = total / banyak
    return rata, max(nilai), min(nilai)

daftar = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        if daftar == []:
            print("Data nilai tidak tersedia.")
        else:
            rata, tertinggi, terendah = rekap_nilai_ujian(*daftar)
            print(f"Rata-rata kelas: {rata}")
            print(f"Nilai tertinggi: {tertinggi}")
            print(f"Nilai terendah: {terendah}")
        break
    try:
        daftar = daftar + [int(masukan)]
    except ValueError:
        daftar = daftar + [float(masukan)]