ALFABET = "abcdefghijklmnopqrstuvwxyz"

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

def cek_kata(teks, kata):
    daftar_indeks = []
    start = 0
    while True:
        i = teks.lower().find(kata.lower(), start)
        if i == -1:
            break
        daftar_indeks.append(i)
        start = i + 1
    return daftar_indeks

def cek_batas_kata(teks, i, panjang):
    if i > 0:                    
        kiri = teks[i - 1]
        if kiri.lower() in ALFABET:   
            return False                       

    posisi_kanan = i + panjang
    if posisi_kanan < len(teks):               
        kanan = teks[posisi_kanan]
        if kanan.lower() in ALFABET:  
            return False                      

    return True

def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    hasil = ""
    posisi = 0
    indeks_tersensor = []

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            potongan_teks = teks[posisi:i]
            efek_sensor = simbol * panjang
            hasil += potongan_teks + efek_sensor

            posisi = i + panjang
            indeks_tersensor.append(i)
    hasil += teks[posisi:]

    return (hasil,len(indeks_tersensor), indeks_tersensor)

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print(f"Jumlah: {jumlah} | Indeks: {indeks}")