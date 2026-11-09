ALFABET = "abcdefghijklmnopqrstuvwxyz"
sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

def cek_sandi(ch, k):
    posisi = ALFABET.find(ch.lower())
    if posisi == -1:
        return ch

    posisi = (posisi + k) % 26
    huruf_baru = ALFABET[posisi]
    if ch == ch.upper():
        return huruf_baru.upper()
    return huruf_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil


print()
print(" Output Deskripsi:", retas_sandi(sandi, kata_kunci))