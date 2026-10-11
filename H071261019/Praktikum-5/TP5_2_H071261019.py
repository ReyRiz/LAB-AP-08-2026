'''Sensor Kata'''

teks = str(input("Masukkan teks: "))
kata = str(input("Masukkan kata target: "))
simbol = str(input("Masukkan simbol: "))

def cek_kata(teks, kata):
    list_indeks_awal = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    panjang = len(kata_lower)

    if panjang == 0:
        return list_indeks_awal
    
    indeks_awal = teks_lower.find(kata_lower)
    while indeks_awal != -1:
        list_indeks_awal.append(indeks_awal)
        indeks_awal = teks_lower.find(kata_lower, indeks_awal + 1)
    return list_indeks_awal

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if i > 0 and teks[i - 1] in alfabet:
        return False 
    batas = i + panjang
    if batas < len(teks) and teks[batas] in alfabet:
        return False
    return True 

def sensor_kata(teks, kata, simbol):
    panjang_kata = len(kata)
    if panjang_kata == 0:
        return teks, 0, []

    posisi_kata = cek_kata(teks, kata)
    indeks_awal = []        
    for posisi in posisi_kata:
        if cek_batas_kata(teks, posisi, panjang_kata):
            indeks_awal.append(posisi)

    teks_tersensor = ""
    i = 0
    while i < len(teks):
        if i in indeks_awal:
            teks_tersensor = teks_tersensor + (simbol * panjang_kata)
            i = i + panjang_kata 
        else:
            teks_tersensor = teks_tersensor + teks[i]
            i = i + 1
    return teks_tersensor, len(indeks_awal), indeks_awal

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print(f"Hasil Teks: {hasil}")
print(f"Jumlah: {jumlah} | Indeks: {indeks}")