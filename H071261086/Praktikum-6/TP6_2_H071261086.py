def daftar_kandidat(kandidat_set, nama):
    nama_bersih = nama.strip().capitalize()
    if not nama_bersih:
        return False
    
    if nama_bersih in kandidat_set:
        print(f"Kandidat '{nama_bersih}' sudah terdaftar!")
        return True

    kandidat_set.add(nama_bersih)
    print(f"'{nama_bersih}' berhasil didaftarkan sebagai kandidat!")
    return True

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_lower = nama_pemilih.lower()
    nama_pemilih_tampil = nama_pemilih.strip().capitalize() if nama_pemilih.strip() else nama_pemilih
    pilihan_cap = pilihan.strip().capitalize()

    if nama_pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih_tampil}' sudah memberikan suara sebelumnya!")
        print()
        return False

    if pilihan_cap not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ditemukan. Suara tidak dicatat.")
        print()
        return False

    rekap_suara[nama_pemilih_lower] = pilihan_cap
    print(f"Suara '{nama_pemilih_tampil}' untuk '{pilihan_cap}' berhasil dicatat!")
    print()
    return True

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for kandidat_dipilih in rekap_suara.values():
        if kandidat_dipilih in perolehan:
            perolehan[kandidat_dipilih] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print()
    print("===================================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("===================================")
    
    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")
    
    total_suara = sum(perolehan.values())
    print()
    print(f"Total suara masuk: {total_suara}")

    if not perolehan:
        print("Tidak ada suara.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]

    if len(pemenang) > 1:
        print(f"HASIL SERI antara {', '.join(pemenang)} dengan {suara_tertinggi} suara! Perlu pemilihan ulang.")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

    print("===================================")

def main():
    kandidat_set = set()
    rekap_suara = {}

    print("===================================")
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("===================================")
    print()
    print("--- FASE PENDAFTARAN KANDIDAT ---")

    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)
    
    print()
    print(f"Kandidat terdaftar: {kandidat_set}")
    print()
    print("--- FASE PEMUNGUTAN SUARA ---")
    print()

    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if nama_pemilih == "":
            break
        
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        
        # cek duplikat dulu sebelum minta kandidat (sesuai test case)
        # tapi fungsi berikan_suara sudah handle semua
        if nama_pemilih.lower() in rekap_suara:
            print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
            print()
            continue

        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

if __name__ == "__main__":
    main()
