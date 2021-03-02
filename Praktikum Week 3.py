#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber = https://koding.alza.web.id/latihan-soal-function-method/

'''
Buatlah sebuah metode yang menerima dua buah bilangan kemudian mencari Kelipatan Persekutuan Terkecil 
(KPK) dari kedua bilangan tersebut.

'''
'''
Input   = Bilangan Pertama
          Bilangan Kedua

Proses  = Menghitung Faktor Persekutuan Terbesar (FPB)
          Menghitung Kelipatan Persekutuan Terkecil (KPK)

Output  = Kelipatan Persekutuan Terkecil (KPK) dari bilangan pertama dan kedua

kpk = a * b / fpb(a,b)
'''

def fpb(a,b):
    if a%b ==0:
        return b
    else:
        return fpb(b,a%b)

def kpk(a,b):
    kpk = a*b / fpb(a,b)
    return int(kpk)

bil1 = int(input("Masukkan Bilangan Pertama: "))
bil2 = int(input("Masukkan BIlangan Kedua: "))
kpk = kpk(bil2,bil1)
print("Kpk dari {} dan {} adalah: {}".format(bil1,bil2,kpk))