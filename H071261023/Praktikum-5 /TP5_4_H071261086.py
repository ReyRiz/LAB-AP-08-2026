def deteksi_anomali_email(email):

    daftar_error = []
    if " " in email:
        daftar_error.append("Tidak boleh mengandung spasi di posisi manapun")

    if email.count("@") > 1 or email.count("@") < 1:
        daftar_error.append("Harus memiliki tepat satu karakter @.")
        return daftar_error  

    local, domain = email.split("@")

    if local == "" or domain == "":
        daftar_error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if local != "":
        if local.startswith(".") or local.endswith(".") or ".." in local:
            daftar_error.append("Bagian local tidak boleh diawali atau diakhiri titik (.) serta tidak boleh mengandung titik berurutan (..).")

    if domain != "":
        # "yermiaborong@gmail.com"
        if "." not in domain:
            daftar_error.append("Bagian domain wajib memiliki minimal satu titik.")
        if ".." in domain or domain.endswith("."):
            daftar_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    email_kecil = email.lower()
    if not (email_kecil.endswith(".com") or email_kecil.endswith(".id") or email_kecil.endswith(".ac.id")):
        daftar_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return daftar_error

def cetak_daftar_email_valid(daftar_email, karakter_border):
    if len(daftar_email) == 0:
        return "Tidak ada email valid."

    panjang_terpanjang = max(len(e) for e in daftar_email)
    lebar_bingkai = panjang_terpanjang + 4  
    baris_atas_bawah = karakter_border * lebar_bingkai
    
    hasil = [baris_atas_bawah]
    for e in daftar_email:
        baris = f"{karakter_border} {e.ljust(panjang_terpanjang)} {karakter_border}"
        hasil.append(baris)
    hasil.append(baris_atas_bawah)

    return "\n".join(hasil)

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email_input = input("Masukkan email: ")
    
    if email_input.lower() == "tutup":
        break

    if email_input in daftar_valid:
        print(">> Email DITOLAK karena:")
        print("   - Email sudah terdaftar (duplikat).")
        continue

    list_anomali = deteksi_anomali_email(email_input)

    if len(list_anomali) > 0:
        print(">> Email DITOLAK karena:")
        for err in list_anomali:
            print(f"   - {err}")
    else:
        print(">> Email VALID!")
        daftar_valid.append(email_input)

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar_email_valid(daftar_valid, border))
