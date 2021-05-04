#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://www.w3resource.com/python-exercises/tuple/python-tuple-exercise-31.php
'''
Buatlah sebuah program yang membuat sebuah list dan dapat
menjumlahkan elemen dari list tersebut dan menjadi tuple

'''
'''
INPUT   = - Memasukkan bilangan yang akan dijumlahkan

PROSES  = - Menjumlahkan elemen yang telah menjadi input

OUTPUT  = - Jumlah elemen yang telah dihitung
'''
x = (1,2,3,4)
y = (3,5,2,1)
z = (2,2,3,1)
a = (0,0,1,2)
print("Listnya adalah sebagai berikut: ")
print(x)
print(y)
print(z)
print(a)
print("\nJumlah elemen dari tuple tersebut adalah : ")
hasil = tuple(map(sum, zip(x,y,z,a)))

print(hasil)