def cek_sandi(ch: str, k: int) -> str:
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    char_lower = ch.lower()

    idx = ALFABET.find(char_lower)

    if idx == -1:
        return ch

    new_idx = (idx + k) % 26
    new_char = ALFABET[new_idx]

    if ch.isupper():
        return new_char.upper()
    return new_char

def mesin_enkripsi(teks: str, k: int) -> str:
    hasil = ""
    for char in teks:
        hasil += cek_sandi(char, k)
    return hasil

def mesin_deskripsi(teks: str, k: int) -> str:
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi: str, kata_kunci: str) -> list[tuple[int, str]]:
    hasil_retas = []
    kata_kunci_lower = kata_kunci.lower()

    for k in range(26):
        pesan_deskripsi = mesin_deskripsi(sandi, k)

        if pesan_deskripsi.lower().find(kata_kunci_lower) != -1:
            hasil_retas.append((k, pesan_deskripsi))

    return hasil_retas

pesan_sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

output = retas_sandi(pesan_sandi, kata_kunci)
print(f"\nOutput Deskripsi: {output}")