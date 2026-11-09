def rekap_nilai(*args):
    if not args:
        return None

    rata_rata = sum(args) / len(args)
    return rata_rata, max(args), min(args)

nilai = []

while True:
    masukkan_nilai_rapor = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()
    if not masukkan_nilai_rapor:
        break
    try:
        nilai.append(float(masukkan_nilai_rapor))
    except ValueError:
        print("Input tidak valid!")

hasil = rekap_nilai(*nilai)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata_rata:.2f}")
    print(f"Nilai tertinggi: {tertinggi:g}")
    print(f"Nilai terendah: {terendah:g}")
