'''OOP (Object-Oriented Programming)'''

class pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective
    ):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor_akhir = (self.nilai_kill * 0.3) + (self.nilai_assist * 0.3) + (self.nilai_objective * 0.4)
        return skor_akhir

    def status_performa(self):
        skor_akhir = self.hitung_skor_akhir()
        if skor_akhir >= 60:
            return "Unggul"
        elif skor_akhir < 60:
            return "Perlu Evaluasi"
        else:
            return "Nilai Luar Biasa"

    def tampilkan_data(self, no):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"\n| {no:<3} | {self.nama:<10} | {self.id_pemain:<12} | {self.role:<10} | {skor_akhir:<10.2f} | {status:<15} |")
        
while True:
    try:
        jumlah_pemain = int(input("Masukkan jumlah pemain: "))
    except ValueError:
        print("Input harus berupa angka.")
        continue

    daftar_pemain = []
    for i in range(jumlah_pemain):
        print(f"\n-- Data Pemain Ke-{i+1} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")

        try:
            kill = float(input("Nilai Kill: "))
            assist = float(input("Nilai Assist: "))
            objective = float(input("Nilai Objective: "))
        except ValueError:
            print("Nilai harus berupa angka. Silakan ulangi input untuk pemain ini.")
            continue

        pemain_baru = pemain(nama, id_pemain, role, kill, assist, objective)
        daftar_pemain.append(pemain_baru)
        jumlah_pemain -= 1

    if jumlah_pemain == 0:
        break

print(f"\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("\n" + "=" * 80)
print(f"\n| {'No':<3} | {'Nama':<10} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
print("\n" + "=" * 80)

for i, Pemain in enumerate(daftar_pemain, start=1):
    Pemain.tampilkan_data(i)

print("\n" + "=" * 80)