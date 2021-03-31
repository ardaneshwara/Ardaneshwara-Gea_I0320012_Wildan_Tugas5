print('Masukkan nilai anda!')
nama = str(input('Masukkan nama lengkap anda: '))
nilai = int(input('Masukkan nilai anda skala 1-100: '))

info = 'Halo, ' + str(nama) + '! ' + 'Nilai anda setelah dikonversi adalah '

#memeriksa nilai
if nilai <= 100 and nilai >84:
    print(info + 'A')
elif nilai <= 84 and nilai >79:
    print(info + 'A-')
elif nilai <= 79 and nilai >74:
    print(info + 'B+')
elif nilai <= 74 and nilai >69:
    print(info + 'B')
elif nilai <= 69 and nilai >64:
    print(info + 'C+')
elif nilai <= 64 and nilai >59:
    print(info + 'C')
elif nilai <= 59 and nilai >=0:
    print(info + 'E')
else:
    print(info + 'nilai tidak valid untuk dikonversi')
print()

