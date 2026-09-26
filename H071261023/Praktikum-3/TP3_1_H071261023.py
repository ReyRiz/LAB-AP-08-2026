#TUGAS 1
print ("--- Rekapitulasi Transaksi Dins Store ---")
print ("ketik '0' untuk menutup tokoh dan mengakhiri sesi.")

while True:
    print()
    try:
        jumlah = int(input("Masukkan jumlah item: "))
    except:
        print("Input harus berupa angka!")
    if jumlah < 0:
        print("Jumlah tidak boleh negatif!")
    elif jumlah > 100:
        print("Maksimal 100 item per transaksi!")
    elif jumlah == 0:
        print("Toko tutup. Sesi rekap selesai.")
        break
    else: 
        print(f"Transaksi {jumlah} item berhasil!")