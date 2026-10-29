
def bersihkan_teks(teks):
    huruf_alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_kecil = teks.lower()
    hasil_bersih = ""

    for karakter in teks_kecil:
        if karakter in huruf_alfabet: 
            hasil_bersih += karakter

    return hasil_bersih

def cek_palinrome(teks):
    teks_dibalik = "".join(reversed(teks))

    if teks == teks_dibalik:
        return (True, -1)
    else:
        for indeks in range(len(teks)):
            if teks[indeks]!= teks_dibalik[indeks]:
                return (False, indeks)

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)

    palindrom_terpanjang = ""
    panjang_terbaik = 0
    indeks_terbaik = 0

    for indeks_awal in range(len(teks_bersih)):
        for indeks_akhir in range(indeks_awal + 1, len(teks_bersih) + 1):
            potongan_teks = teks_bersih[indeks_awal:indeks_akhir]
            status_simetris, _ = cek_palinrome(potongan_teks)
            if status_simetris:
                if len(potongan_teks) > panjang_terbaik:
                    palindrom_terpanjang = potongan_teks
                    panjang_terbaik = len(potongan_teks)
                    indeks_terbaik = indeks_awal

    return {
        "teks": palindrom_terpanjang,
        "panjang": panjang_terbaik,
        "indeks_awal": indeks_terbaik
    }

input_masukan = input("Input Masukan: ")

teks_bersih_hasil = bersihkan_teks(input_masukan)
print("Teks Bersih:", teks_bersih_hasil)

output_terharap = inti_palinrome(input_masukan)
print("Output Terharap:", output_terharap)
