'''Validasi Email'''

print("--- Sistem Pencatatan Email Valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.\n")

def deteksi_anomali_email(email):
    anomali = []
    if email.count("@") != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        return anomali
    elif " " in email:
        anomali.append("Tidak boleh mengandung spasi!")
        return anomali

    local, domain = email.split('@')
    domain_resmi = ('.com', '.id', '.ac.id')

    if not local or not domain:
        anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if '.' not in domain:
        anomali.append("Bagian domain wajib memiliki minimal satu titik.")
    if domain:
        if '..' in domain or domain.endswith('.'):
            anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if local:
        if local.startswith('.') or local.endswith('.'):
            anomali.append("Bagian local tidak boleh diawali atau diakhiri titik (.).")
        elif '..' in local:
            anomali.append("Bagian local tidak boleh mengandung titik berurutan (..).")
    if not domain.endswith(domain_resmi):
            anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
    return anomali

def program_validasi_email():
    daftar_email_valid = []
    while True:
        email = str(input("Masukkan email: "))
        anomali = deteksi_anomali_email(email)

        if email.lower() == "tutup":
            break
        
        if not anomali and email in daftar_email_valid:
                anomali.append("Email sudah terdaftar (Duplikat).")
        if not anomali:
            daftar_email_valid.append(email)
            print(">> Email VALID!")
        else:
            print(">> Email DITOLAK karena:")
            for error in anomali:
                print(f"   - {error}")

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return
    
    lebar_maks = max(len(email) for email in daftar_email_valid)
    panjang_baris = lebar_maks + 4  # padding 2 spasi di kiri dan kanan
    
    print(f"\n--- HASIL EMAIL VALID ---")
    print(f"+{karakter_border * (panjang_baris-2)}+")
    for email in daftar_email_valid:
        print(f"| {email:<{lebar_maks}} |")
    print(f"+{karakter_border * (panjang_baris-2)}+")


    cetak_daftar(daftar_email_valid, karakter_border)
    
program_validasi_email()