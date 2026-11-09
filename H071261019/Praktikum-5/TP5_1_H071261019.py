'''Pembersihan Teks'''

teks = str(input("Masukkan teks prasasti: "))

def bersihkan_teks(teks):
    teks = teks.lower()  
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for huruf in teks: 
        if huruf in alfabet:
            teks_bersih = teks_bersih + huruf
    return teks_bersih

def cek_palindrom(teks):
    teks_dibalik = "".join(reversed(teks))
    if teks == teks_dibalik:
        return True, -1
    for indeks_pertama_beda in range (len(teks)):
        if teks[indeks_pertama_beda] != teks_dibalik[indeks_pertama_beda]:
            return False, indeks_pertama_beda

def inti_palindrom(teks):
    teks_bersih = bersihkan_teks(teks)
    n = len(teks_bersih)
    
    for panjang in range (n, 0, -1):
        for indeks in range (n - panjang + 1):
            substring = teks_bersih[indeks : indeks + panjang]
            palindrom, _ = cek_palindrom(substring)
            if palindrom == True:
                return {
                    "teks": substring,
                    "panjang": panjang,
                    "indeks_awal": indeks
                }

hasil = inti_palindrom(teks)
print(f"\nTeks bersih: {bersihkan_teks(teks)}")
print(f"Output terharap: {hasil}")

