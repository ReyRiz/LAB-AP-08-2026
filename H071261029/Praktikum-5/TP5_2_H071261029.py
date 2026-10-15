def cek_kata(teks: str, kata: str) -> list[int]:
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    daftar_indeks = []
    posisi_awal = 0

    while True:
        posisi = teks_kecil.find(kata_kecil, posisi_awal)
        if posisi == -1:
            break
        daftar_indeks.append(posisi)
        posisi_awal = posisi + 1

    return daftar_indeks

def cek_batas_kata(teks: str, i: int, panjang: int) -> bool:
    daftar_huruf = "abcdefghijklmnopqrstuvwxyz"

    if i > 0:
        karakter_sebelum = teks[i - 1].lower()
        if karakter_sebelum in daftar_huruf:
            return False

    if i + panjang < len(teks):
        karakter_sesudah = teks[i + panjang].lower()
        if karakter_sesudah in daftar_huruf:
            return False

    return True

def sensor_kata(teks: str, kata: str, simbol: str) -> tuple[str, int, list[int]]:
    panjang_kata = len(kata)
    semua_indeks = cek_kata(teks, kata)

    indeks_valid = []

    for idx in semua_indeks:
        if cek_batas_kata(teks, idx, panjang_kata):
            indeks_valid.append(idx)

    teks_tersensor = ""
    indeks_terakhir = 0

    for idx in indeks_valid:
        teks_tersensor += teks[indeks_terakhir:idx]
        teks_tersensor += simbol * panjang_kata
        indeks_terakhir = idx + panjang_kata
    teks_tersensor += teks[indeks_terakhir:]

    return teks_tersensor, len(indeks_valid), indeks_valid

teks_input = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_input = input("Masukkan simbol: ")

hasil_teks, jumlah, list_indeks = sensor_kata(teks_input, kata_target, simbol_input)

print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah} | Indeks: {list_indeks}")