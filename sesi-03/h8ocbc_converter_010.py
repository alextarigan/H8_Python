def convertToCK(suhu,skala):
    """
    Function yang mengkonversi suhu ,
    memiliki 2 argumen (suhu dan suhu tujuan)
    """
    if skala == 'K':
        total = suhu + 273
    elif skala == 'C':
        total = suhu - 273
    print('Hasil Konversi : {} {}'.format(total,skala))


def convertToFahrenheit(suhu,skala):
    """
    Function yang mengkonversi suhu ke fahrenheit,
    memiliki 2 argumen (suhu dan suhu yang ingin dikonversi)
    """
    if skala == 'C':
        total = 9/5 * suhu + 32
    elif skala == 'K':
        total = 9/5 * (suhu-273) + 32
    print('Hasil Konversi : {} Fahrenheit'.format(total))

def convertFromFahrenheit(suhu,tujuan):
    """
    Function yang dapat mengkonversi suhu 
    dari fahrenheit ke Celcius(C) dan Kelvin(K)
    """
    if tujuan == 'C':
        total = (5/9) * suhu -32
    elif tujuan == 'K':
        total = (5/9) * (suhu-32) + 273
    print('Hasil Konversi : {}{}'.format(total,tujuan))

if __name__ == "__main__":
    pilihan = -1
    while True:
        print('Selamat Datang di Program Konversi\n')
        print('1. Konversi suhu dari Celcius ke Kelvin atau Kelvin ke Celcius\n')
        print('2. Konversi Suhu ke Fahrenheit dari Celcius atau Kelvin\n')
        print('3. Konversi Suhu dari Fahrenheit ke Celcius atau Kelvin\n')
        print('0. Keluar\n')
        pilihan = int(input('Masukkan pilihan : '))
        if pilihan == 1:
            suhu = int(input("Masukkan Jumlah suhu : "))
            skala = str(input("Masukkan Suhu Tujuan (C/K):"))
            print('Konversi dari Celcius ke Kelvin atau Kelvin ke Celcius')
            convertToCK(suhu,skala)            
        elif pilihan == 2:
            suhu = int(input("Masukkan Jumlah suhu : "))
            skala = str(input("Masukkan Suhu asal (C/K):"))
            print('Konversi Ke Fahrenheit\n')
            convertToFahrenheit(suhu,skala)
        elif pilihan == 3:
            suhu = int(input("Masukkan Jumlah suhu(Fahrenheit) : "))
            skala = str(input("Masukkan Suhu tujuan (C/K):"))
            print('Konversi dari Fahrenheit\n')
            convertFromFahrenheit(suhu,skala)
        elif pilihan == 0:
            print('Terima kasih')
            break
        else:
            print('Silahkan input angka yang benar\n')
            continue