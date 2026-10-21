'''Sistem Pemilihan Ketua Kelas "VoteClass"'''

def daftar_kandidat(kandidat_set, nama):
    nama_kandidat = nama.capitalize()
    if nama_kandidat:
        kandidat_set.add(nama_kandidat)

    print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")
    return kandidat_set

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_asli = nama_pemilih.lower()
    if pemilih_asli in rekap_suara:
        print("Pemilih sudah terdaftar!\n")
        return rekap_suara
    
    if pilihan.capitalize() not in kandidat_set:
        print("Kandidat tidak terdaftar!\n")
        return rekap_suara

    rekap_suara[pemilih_asli] = pilihan.capitalize()
    print(f"Suara '{pemilih_asli.capitalize()}' untuk '{pilihan.capitalize()}' berhasil dicacat!\n")
    return rekap_suara

def hitung_suara(rekap_suara, kandidat_set):
    hasil = {kandidat : 0 for kandidat in kandidat_set}
    for kandidat_terpilih in rekap_suara.values():
        if kandidat_terpilih in hasil:
            hasil[kandidat_terpilih] += 1
    return hasil

def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("       HASIL PEMILIHAN KETUA KELAS      ")
    print("========================================")
    total_suara = sum(perolehan.values())
    
    for kandidat, jumlah in perolehan.items():
        print(f"    {kandidat}: {jumlah} suara")
    print(f"\nTotal Suara Masuk: {total_suara}")
    
    if total_suara == 0:
        print("Tidak ada suara yang masuk.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [kandidat for kandidat, suara in perolehan.items() if suara == suara_tertinggi]
    
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]}!")
def main():
    kandidat_set = set()
    rekap_suara = {}

    print("========================================")
    print("      SISTEM PEMILIHAN KETUA KELAS      ")
    print("========================================")

    print("\n--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama == "":
            break
        kandidat_set = daftar_kandidat(kandidat_set, nama)
    print(f"\nKandidat terdaftar: {kandidat_set}")


    print("\n--- FASE PEMUNGUTAN SUARA ---\n")
    while True:
        pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if pemilih == "":
            break
        print(f"Kandidat tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        rekap_suara = berikan_suara(rekap_suara, kandidat_set, pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

main()
    