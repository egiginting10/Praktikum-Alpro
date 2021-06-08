#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://www.w3resource.com/python-exercises/re/python-re-exercise-53.php

'''
Egi adalah sebuah mahasiswa Teknik Informatika di Universitas Kristen Duta Wacana
saat ini dia ingin membuat sebuah pemrograman yang dapat menghapus huruf kecil didalam
sebuah kalimat.Bantulah Egi untuk membuat program tersebut.
'''
'''
INPUT   = - Kalimat yang akan diubah

PROSES  = - Program akan mencari huruf kecil dan akan menghapusnya

OUTPUT  = - Kalimat setelah huruf kecil dihapus
'''
import re
str1 = 'EGI ADALAH SEBUAH MAHASISWA TEKNIK INFORMATIKA DI UNIVERSITAS KRISTEN DUTA WACANA'
print("Kalimat Pertama adalah : ")
print(str1)
print("Kalimat setelah penghapusan huruf kecil adalah : ")
remove_lower = lambda text: re.sub('[a-z]','',text)
result = remove_lower(str1)
print(result)
