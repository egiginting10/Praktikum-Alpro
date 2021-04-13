#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://pesonainformatika.com/programming/membuat-program-daftar-belanja-menggunakan-python/

'''
Buatlah sebuah program daftar belanja yang dapat menginputkan data
yang mereka inputkan di Daftar Belanja.Simpan data yang telah diinputkan oleh user
ke dalam file text(belanja.txt).
'''
'''
Input   = - Daftar Belanjaan

Proses  = - Menginput Daftar Belanjaan => Disimpan kedalam file txt
          - Mengulangi inputan pertama apabila user memasukkan menu 1
          - dst... 

Output  = - Menampilkan file yang berisi list belanjaan

'''
def tambah_belanja(text):
    file = open('belanja.txt', 'a+')
    file.write('\n' + text)

def daftar_belanja():
    file = open('belanja.txt', 'a+')
    file.seek(0)
    text = file.read()
    print(text)

def tanya_pengguna():
    print('Silahkan Masukkan Keperluan Belanja anda ke daftar belanja')
    print('==================== Daftar Belanja ====================')
    tambah_belanja(input('Mau belanja apa? : '))

loop = True

print('=============== Menu ===============')
print('1. Tambah ke Daftar Belanja')
print('2. List Belanja')
print('3. Quit/Keluar')
while(loop):
    print('\n')
    menu = input('Masukkan menu : ')

    if menu == "1":
        tanya_pengguna()
    elif menu == "2":
        daftar_belanja()
    elif menu == "3":
        quit()
    
    else:
        print("Menu tidak tersedia!")