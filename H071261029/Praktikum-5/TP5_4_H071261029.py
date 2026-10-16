def deteksi_anomali_email(email: str, daftar_email_valid: list[str]) -> list[str]:
    daftar_anomali = []

    if email in daftar_email_valid:
        daftar_anomali.append("Email sudah terdaftar (Duplikat).")

    if " " in email:
        daftar_anomali.append("Tidak boleh mengandung spasi di posisi manapun.")

    jumlah_at = email.count("@")
    if jumlah_at != 1:
        daftar_anomali.append("Harus memiliki tepat satu karakter @.")
    else:
        local, domain = email.split("@")

        if len(local) == 0 or len(domain) == 0:
            daftar_anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

        if len(local) > 0:
            if local.startswith(".") or local.endswith(".") or ".." in local:
                daftar_anomali.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

        if "." not in domain:
            daftar_anomali.append("Bagian domain wajib memiliki minimal satu titik.")

        if ".." in domain or (len(domain) > 0 and domain.endswith(".")):
            daftar_anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik")

        if not (domain.endswith(".com") or domain.endswith(".id") or domain.endswith(".ac.id")):
            daftar_anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return daftar_anomali

def cetak_daftar(daftar_email_valid: list[str], karakter_border: str) -> str:
    if not daftar_email_valid:
        return "Tidak ada email valid yang terdaftar."

    panjang_maksimal = max(len(email) for email in daftar_email_valid)
    lebar_dalam = panjang_maksimal + 4
    garis_bingkai = "+" + (karakter_border * lebar_dalam) + "+"

    daftar_baris = [garis_bingkai]

    for email in daftar_email_valid:
        daftar_baris.append(f"| {email:<{panjang_maksimal + 2}} |")
    daftar_baris.append(garis_bingkai)

    return "\n".join(daftar_baris)

print("--- Sistem Pencatatan Email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ").strip()
if not karakter_border:
    karakter_border = "="

print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email_valid = []

while True:
    masukan_email = input("Masukkan email: ").strip()

    if masukan_email.lower() == "tutup":
        break

    daftar_anomali = deteksi_anomali_email(masukan_email, daftar_email_valid)

    if daftar_anomali:
        print(">> Email DITOLAK karena:")
        for pesan_error in daftar_anomali:
            print(f"    - {pesan_error}")
    else:
        print(">> Email VALID!")
        daftar_email_valid.append(masukan_email)

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_email_valid, karakter_border))