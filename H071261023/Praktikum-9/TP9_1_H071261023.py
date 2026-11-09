print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")

class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<10} | {self.role:<10} | {self.hitung_skor_akhir():<10.2f} | {self.status_performa():<15} |")

data_pemain = []

while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        else:
            break
    except:
        print("Input yang anda masukkan tidak valid!")

pemain = 1
while pemain <= jumlah_pemain:
    try:
        print(f"\n-- Data Pemain ke-{pemain} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = int(input("Nilai Kill: "))
        nilai_assist = int(input("Nilai Assist: "))
        nilai_objective = int(input("Nilai Objective: "))

        isi_data_pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        data_pemain.append(isi_data_pemain)
        pemain += 1
    except:
        print("Input yang anda masukkan tidak valid!")
        continue

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 77)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
print("=" * 77)

i = 0
while i < len(data_pemain):
    data_pemain[i].tampilkan_data(i + 1)
    i += 1
    
print("=" * 77)