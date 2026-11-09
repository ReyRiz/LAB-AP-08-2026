print("========================================")
print("      SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")
kandidat = set()
rekap_suara = {}

def daftar_kandidat(kandidat_set, nama):
    nama_formatted = nama.capitalize()
    kandidat_set.add(nama_formatted)
    print(f"'{nama_formatted}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama = nama_pemilih.capitalize()
    pilihan_formatted = pilihan.capitalize()

    if nama in rekap_suara:
        print(f"'{nama}' sudah memberikan suara sebelumnya!")
    elif pilihan_formatted not in kandidat_set:
        print("Kandidat tidak ditemukan!")
    else:
        rekap_suara[nama] = pilihan_formatted
        print(f"Suara '{nama}' untuk '{pilihan_formatted}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    hasil = {k: 0 for k in kandidat_set}
    for pilihan in rekap_suara.values():
        if pilihan in hasil:
            hasil[pilihan] += 1
    return hasil

def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("       HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    if not perolehan:
        print("Belum ada kandidat!")
        return

    for nama, suara in sorted(perolehan.items()):
        print(f"{nama}: {suara} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    suara_tertinggi = max(perolehan.values())
    pemenang = [nama for nama, suara in perolehan.items() if suara == suara_tertinggi]

    if suara_tertinggi == 0:
        print("Belum ada suara yang masuk.")
    elif len(pemenang) > 1:
        print(f"Hasil seri antara {', '.join(pemenang)} dengan {suara_tertinggi} suara!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

    print("========================================")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama == "":
        break
    daftar_kandidat(kandidat, nama)

print(f"Kandidat terdaftar: {kandidat}")

print("\n--- FASE PEMUNGUTAN SUARA ---")
if len(kandidat) < 2:
    print("Minimal harus ada 2 kandidat untuk memulai voting!")
else:
    while True:
        nama = input("\nNama pemilih (kosongkan untuk selesai): ")
        if nama == "":
            break

        print(f"Kandidat yang tersedia: {kandidat}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat, nama, pilihan)

    hasil = hitung_suara(rekap_suara, kandidat)
    tampilkan_hasil(hasil)