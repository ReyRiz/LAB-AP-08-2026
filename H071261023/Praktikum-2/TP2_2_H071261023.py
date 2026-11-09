jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan Express (ya/tidak): ")

if jarak <5 :
    tarif_jarak = 10000
elif jarak >=5 and jarak <=20:
    tarif_jarak = 20000
else :
    tarif_jarak = 35000

biaya_layanan = 15000 if express == "ya" else 0
tarif = tarif_jarak + biaya_layanan
print ("Total tarif pengiriman: Rp.",tarif)