print("--- Rekapitulasi Transaksi Dins Store ---")
while True:
    try:
        jumlah_item = int(input("Masukkan jumlah item (ketik 0 untuk mengakhiri sesi): "))
        if jumlah_item == 0:
            print("Sesi selesai, terima kasih")
            break
        elif jumlah_item < 0:
            print("Jumlah tidak boleh negatif!")
        elif jumlah_item > 0 and jumlah_item <= 100:
            print("Transaksi", jumlah_item, "item selesai")
        elif jumlah_item > 100:
            print("Maksimal 100 item per transaksi!")
    except ValueError:
        print("Input harus berupa angka!")
        
   
