ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k): 
    ch_kecil = ch.lower()
    
    posisi_huruf = ALFABET.find(ch_kecil)
    if posisi_huruf == -1:
        return ch

    posisi_baru = (posisi_huruf + k) % 26
    huruf_hasil = ALFABET[posisi_baru]
    return huruf_hasil.lower()

def mesin_enkripsi(teks, k):
    teks_hasil = ""
    for karakter in teks:
        karakter_geser = cek_sandi(karakter, k)
        teks_hasil = teks_hasil + karakter_geser
    return teks_hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    daftar_hasil = []
    kata_kunci_kecil = kata_kunci.lower()

    for kunci in range(26):
        teks_coba = mesin_dekripsi(sandi, kunci)
        if teks_coba.lower().find(kata_kunci_kecil) != -1:
            daftar_hasil.append((kunci, teks_coba))

    return daftar_hasil

pesan_tersita = input("Masukkan pesan tersita: ")
kata_target = input("Masukkan kata kunci target: ")

output_deskripsi = retas_sandi(pesan_tersita, kata_target)
print(f"Output Deskripsi: {output_deskripsi}")

