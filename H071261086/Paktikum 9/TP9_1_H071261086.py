class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id = id_pemain
        self.role = role
        self.kill = nilai_kill
        self.assist = nilai_assist
        self.objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
    
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no}  | {self.nama:<10} | {self.id:<10} | {self.role:<15} | {skor:<10.2f} | {status:<15} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

jumlah = int(input("Masukkan jumlah pemain: "))

daftar_pemain = []

for i in range(jumlah):
    print()
    print(f"-- Data Pemain ke-{i+1} --")
    nama = input("Nama: ")
    id = input("ID Pemain: ")
    role = input("Role: ")
    kill = int(input("Nilai Kill: "))
    assist = int(input("Nilai Assist: "))
    objektif = int(input("Nilai Objective: "))

    pemain = Pemain(nama, id, role, kill, assist, objektif)   
    daftar_pemain.append(pemain)

print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 81)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<15} | {'Skor Akhir':<10} | {'Status':<15} |")
print("=" * 81)

for nomor, player in enumerate(daftar_pemain, start=1):
    player.tampilkan_data(nomor)
print("=" * 81)
