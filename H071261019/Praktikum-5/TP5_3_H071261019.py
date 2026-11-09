'''Brute Force Sandi Caesar Cipher'''

teks = str(input("Masukkan pesan tersita (enkripsi Caesar): "))
kata_kunci = str(input("Masukkan kata kunci target: "))

def cek_sandi(ch, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cek = alphabet.find(ch.lower())
    if cek == -1:
        return ch
    hasil_cek = (cek + k) % 26
    karakter_baru = alphabet[hasil_cek]
    return karakter_baru.upper() if ch.isupper() else karakter_baru

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan_dekripsi = mesin_dekripsi(sandi, k)
        if pesan_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan_dekripsi))
    return hasil

hasil_retas = retas_sandi(teks, kata_kunci)
print(f"\nOutput Dekripsi: {hasil_retas}")

