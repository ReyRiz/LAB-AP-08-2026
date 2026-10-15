def bersihkan_teks(teks):
    daftar_huruf = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for karakter in teks:
        karakter_kecil = karakter.lower()

        if karakter_kecil in daftar_huruf:
            teks_bersih += karakter_kecil

    return teks_bersih

def cek_palinrome(teks:str) -> tuple[bool, int]:
    teks_terbalik = "".join(reversed(teks))
    if teks == teks_terbalik:
        return True, -1
    else:
        total_huruf = len(teks)
        for i in range(total_huruf):
            if teks[i] != teks_terbalik[i]:
                return False, i
        return False, 0

def inti_palinrome(teks: str) -> dict:
    panjang_maksimal = 0
    kata_terpanjang = ""
    indeks_awal_terbalik = 0

    total_huruf = len(teks)

    for i in range(total_huruf):
        for j in range(i + 1, total_huruf + 1):
            potongan_kata = teks[i:j]
            apakah_palindrom, _ = cek_palinrome(potongan_kata)

            if apakah_palindrom:
                if len(potongan_kata) > panjang_maksimal:
                    panjang_maksimal = len(potongan_kata)
                    kata_terpanjang = potongan_kata
                    indeks_awal_terbalik = i

    return {
        "teks": kata_terpanjang,
        "panjang": panjang_maksimal,
        "indeks_awal": indeks_awal_terbalik
    }

prasasti = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(prasasti)

print(f"\nTeks Bersih: {teks_bersih}")
hasil_palindrom = inti_palinrome(teks_bersih)
print(f"Output Terharap: {hasil_palindrom}")