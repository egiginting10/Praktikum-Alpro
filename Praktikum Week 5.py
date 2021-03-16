#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://student.blog.dinus.ac.id/fanuelphalosa/2019/12/21/contoh-soal-perulangan-pada-python/

'''
Canny merupakan anak kost. Dia memiliki total saldo uang bulanan yang diberikan oleh orang tuanya. 
Setiap bulan ada saja pengeluaran yang dikeluarkan olehnya. Buat program untuk
membantu Canny menghitung sisa saldo uang bulanannya setelah mengeluarkan beberapa uang pengeluaran.
NB:user dapat menginputkan pengeluaran berkali – kali dan tekan 1 untuk keluar
'''
'''
Input   = - Saldo Awal
          
Proses  = - Menghitung Pengeluaran

Output  = - Sisa Saldo
'''

saldo_awal = int(input("Masukkan Saldo Awal : Rp "))
sisa = saldo_awal
while(True):
    pengeluaran = int(input("Masukkan Pengeluaran Hari ini (tekan 1 untuk keluar): "))
    if pengeluaran == 1:
        print("Sisa saldo = Rp ",sisa)
        break
    sisa = sisa - pengeluaran
    if sisa < 0 :
        print("Saldo Tidak Mencukupi")
        print("Sisa Saldo adalah Rp",sisa + pengeluaran)
        break
