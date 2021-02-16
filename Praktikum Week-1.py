#Nama : Egi Granaldi Ginting
#Universitas Kristen Duta Wacana
#Sumber : https://elearning.ukdw.ac.id/pluginfile.php/39811/mod_assign/introattachment/0/soal%20A.docx.pdf?forcedownload=1

'''
Pada suatu hari, Ibu meminta Galih untuk mengajari adiknya. Adiknya kesulitan mengerjakan
soal fisika. Akan tetapi Galih juga kesulitan mengerjakan soal tersebut sehingga Galih meminta
tolong kepada Anda untuk membuatkan sebuah program. Program yang diinginkan Galih adalah
program yang dapat menghitung percepatan partikel.

Rumus percepatan : (Vt**2 - V0**2) / (2*s)

Vt = Kecepatan Akhir
V0 = Kecepatan Awal
s  = Jarak yang ditempuh

'''
'''
Input   : Vt ; V0 ; s

Proses  : - Memasukkan Kecepatan akhir
          - Memasukkan Kecepatan Awal
          - Memasukkan Jarak yang akan ditempuh

Output  : Percepatan Partikel setelah terjadi perubahan kecepatan
'''

Vt = int(input("Kecepatan Akhir (m/s) :"))
V0 = int(input("Kecepatan Awal (m/s) :"))
s  = int(input("Jarak Tempuh (m) :"))
percepatan = (Vt**2 - V0**2) / (2*s)
print("Jadi Percepatannya adalah:",percepatan,"m/s^2")







