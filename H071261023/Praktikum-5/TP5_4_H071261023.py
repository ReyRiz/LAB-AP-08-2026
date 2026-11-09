print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")

print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

def deteksi_anomali_email(email):
    error = []

    if " " in email:
        error.append("Tidak boleh mengandung spasi.")
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error
    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        error.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")
    if "." not in domain:
        error.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (email.endswith(".com") or email.endswith(".id")):
        error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return error

def cetak_daftar(daftar_email_valid, karakter_border):
    lebar = len(max(daftar_email_valid, key=len))
    garis = "+" + karakter_border * (lebar + 2) + "+"

    hasil = garis
    for email in daftar_email_valid:
        hasil += "\n| " + email.ljust(lebar) + " |"
    hasil += "\n" + garis
    return hasil

daftar_valid = []

while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break
    error = deteksi_anomali_email(email)

    if len(error) == 0 and email in daftar_valid:
        error.append("Email sudah terdaftar (Duplikat).")

    if len(error) == 0:
        daftar_valid.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for pesan in error:
            print("   - " + pesan)

print()
print("--- HASIL EMAIL VALID ---")
if len(daftar_valid) == 0:
    print("Tidak ada email valid.")
else:
    print(cetak_daftar(daftar_valid, border))