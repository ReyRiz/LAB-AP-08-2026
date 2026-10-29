def hitung_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []

while True:
    nilai = input("Masukkan nilai ujian siswa: ")
    if nilai == "":
        break

    daftar_nilai.append(float(nilai))

if (nilai) == 0:
    print("Data nilai tidak tersedia")
else:
    rata_rata, tertinggi, terendah = hitung_nilai(*daftar_nilai)
    if rata_rata.is_integer():
        rata_rata = int(rata_rata)

    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {int(tertinggi)}")
    print(f"Nilai terendah: {int(terendah)}")
