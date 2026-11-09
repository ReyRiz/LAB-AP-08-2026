ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks :
        if ch.lower() in ALFABET:
            hasil += ch.lower()
    return hasil

def cek_palinrome(teks):
    balik = "".join(reversed(teks))
    for i in range(len(teks)):
        if teks[i] != balik[i]:
            indeks_pertama_beda = i
            return (False, indeks_pertama_beda)
    return (True, -1)

def inti_palinrome(teks):
    hasil = {"teks": "", "panjang": 0, "indeks_awal": 0}
   
    for awal in range(len(teks)):
        for akhir in range(awal + 1, len(teks) + 1):
            potongan = teks[awal:akhir]
            palindrom, _ = cek_palinrome(potongan)
            if palindrom and len(potongan) > hasil["panjang"]:
                hasil = {"teks": potongan, "panjang": len(potongan), "indeks_awal": awal}

    return hasil

teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih))