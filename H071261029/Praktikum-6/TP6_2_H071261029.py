def daftar_kandidat(kandidat_set: set, nama: str) -> bool:
    nama_terformat = nama.strip().capitalize()
    
    if nama_terformat in kandidat_set:
        print(f">> Error: Kandidat '{nama_terformat}' sudah terdaftar sebelumnya!")
        return False

    kandidat_set.add(nama_terformat)
    print(f"'{nama_terformat}' berhasil didaftarkan sebagai kandidat!")
    return True


def berikan_suara(rekap_suara: dict, kandidat_set: set, nama_pemilih: str, pilihan: str) -> bool:
    nama_pemilih_terformat = nama_pemilih.strip().lower()
    nama_pilihan_terformat = pilihan.strip().capitalize()

    if nama_pemilih_terformat in rekap_suara:
        print(f"'{nama_pemilih.strip().capitalize()}' sudah memberikan suara sebelumnya!")
        return False

    if nama_pilihan_terformat not in kandidat_set:
        print(f">> Error: Kandidat '{nama_pilihan_terformat}' tidak ditemukan di daftar kandidat!")
        return False

    rekap_suara[nama_pemilih_terformat] = nama_pilihan_terformat
    print(f"Suara '{nama_pemilih.strip().capitalize()}' untuk '{nama_pilihan_terformat}' berhasil dicatat!")
    return True


def hitung_suara(rekap_suara: dict, kandidat_set: set) -> dict:
    perolehan_suara = {kandidat: 0 for kandidat in kandidat_set}

    for kandidat_pilihan in rekap_suara.values():
        if kandidat_pilihan in perolehan_suara:
            perolehan_suara[kandidat_pilihan] += 1

    return perolehan_suara


def tampilkan_hasil(perolehan: dict) -> None:
    print("\n========================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total_suara_masuk = sum(perolehan.values())

    for kandidat, jumlah_suara in perolehan.items():
        print(f"   {kandidat}: {jumlah_suara} suara")

    print(f"Total suara masuk: {total_suara_masuk}")

    if total_suara_masuk == 0:
        print("Tidak ada suara yang masuk.")
        print("========================================")
        return

    suara_tertinggi = max(perolehan.values())

    kandidat_pemenang = []
    for kandidat, suara in perolehan.items():
        if suara == suara_tertinggi:
            kandidat_pemenang.append(kandidat)

    if len(kandidat_pemenang) > 1:
        daftar_seri = ", ".join(kandidat_pemenang)
        print(f"Hasil SERI antara: {daftar_seri}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {kandidat_pemenang[0]} dengan {suara_tertinggi} suara!")

    print("========================================")


print("========================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

kandidat_set = set()
rekap_suara = {}

print("\n--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama_kandidat = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()

    if not nama_kandidat:
        if len(kandidat_set) < 2:
            print(">> Error: Minimal harus ada 2 kandidat sebelum pemungutan suara dimulai!")
            continue
        break

    daftar_kandidat(kandidat_set, nama_kandidat)

print(f"Kandidat terdaftar: {kandidat_set}")

print("\n--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()

    if not nama_pemilih:
        break

    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan_kandidat = input("Pilih kandidat: ").strip()

    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan_kandidat)

hasil_perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(hasil_perolehan)