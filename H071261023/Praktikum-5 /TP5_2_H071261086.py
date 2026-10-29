
def cek_kata(teks, kata):
    teks_kecil = teks.lower() 
    kata_kecil = kata.lower()
    
    daftar_indeks = []
    posisi_cari = 0

    while True:
        indeks_ditemukan = teks_kecil.find(kata_kecil, posisi_cari)
        if indeks_ditemukan == -1:
            break
        daftar_indeks.append(indeks_ditemukan)
        posisi_cari = indeks_ditemukan + 1  
    return daftar_indeks

def cek_batas_kata(teks, i, panjang):
    huruf_alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if i == 0:
        batas_kiri_ok = True
    else:
        karakter_sebelum = teks[i - 1]
        if karakter_sebelum in huruf_alfabet:
            batas_kiri_ok = False
        else:
            batas_kiri_ok = True

    posisi_akhir = i + panjang
    if posisi_akhir >= len(teks):
        batas_kanan_ok = True
    else:
        karakter_sesudah = teks[posisi_akhir]
        if karakter_sesudah in huruf_alfabet:
            batas_kanan_ok = False
        else:
            batas_kanan_ok = True

    return batas_kiri_ok and batas_kanan_ok

def sensor_kata(teks, kata, simbol):
    daftar_mentah = cek_kata(teks, kata)
     
    daftar_indeks_valid = []
    for indeks in daftar_mentah:
        if cek_batas_kata(teks, indeks, len(kata)):
            daftar_indeks_valid.append(indeks)

    teks_tersensor = ""
    posisi_sekarang = 0
    sensor_pengisi = simbol * len(kata)

    for indeks_sensor in daftar_indeks_valid:
        potongan_awal = teks[posisi_sekarang:indeks_sensor]
        teks_tersensor = teks_tersensor + potongan_awal + sensor_pengisi
        posisi_sekarang = indeks_sensor + len(kata)

    sisa_teks = teks[posisi_sekarang:]
    teks_tersensor = teks_tersensor + sisa_teks

    jumlah_tersensor = len(daftar_indeks_valid)

    return (teks_tersensor, jumlah_tersensor, daftar_indeks_valid)

teks_asli = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_sensor = input("Masukkan simbol: ")

hasil_teks, jumlah, list_indeks = sensor_kata(teks_asli, kata_target, simbol_sensor)

print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah} | Indeks: {list_indeks}")
