
print('=== Koversi Suhu ===')

def konversi_suhu(suhu, skala_asal, skala_tujuan):
    '''fitur konversi suhu'''
    skala_valid = ['C','F','K']
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError('''Skala suhu tidak dikenali.''')
    
    if skala_asal == 'C':
        if skala_tujuan == 'F':
            suhu = suhu * 9/5 + 32
            return suhu
        elif skala_tujuan == 'K':
            suhu = suhu + 273.15
            return suhu
    elif skala_asal == 'F':
        if skala_tujuan == 'C':
            suhu = (suhu - 32) * 5/9
            return suhu
        elif skala_tujuan == 'K':
            suhu = (suhu - 32) * 5/9 + 273.15
            return suhu
    elif skala_asal == 'K':
        if skala_tujuan == 'C':
            suhu = suhu - 273.15
            return suhu
        elif skala_tujuan == 'F':
            suhu = (suhu - 273.15) * 9/5 + 32
            return suhu

status = True
while status:
    input_suhu = input('Masukkan suhu (atau "selesai" untuk keluar): ')
    if input_suhu == 'selesai':
        status = False
    skala_asal = input('Skala asal (C/F/K): ')
    skala_tujuan = input('Skala tujuan (C/F/K): ')

    try:
        suhu = float(input_suhu)
        hasil_konversi = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f'Hasil: {suhu} {skala_asal} = {hasil_konversi} {skala_tujuan}')
    except ValueError:
        print('Error: Skala suhu tidak dikenali')
        continue
    
