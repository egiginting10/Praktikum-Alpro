#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber = "Saya Sendiri"

'''
Buatlah sebuah program yang meminta input jarak tempuh kereta api, kemudian program tersebut akan menentukan berapakah 
harga tiket yang akan dibayarkan sesuai dengan jarak yang ditempuh.Untuk pembelian di atas jarak 301 km - 400 km mendapatkan diskon 20%.
Pembelian di atas jarak 200 km - 300 km mendapatkan diskon 15%.Pembelian di atas jarak 0 km - 199 km tidak mendapatkan diskon sama sekali.
Harga tiket kereta api adalah Rp 300.000,00.
Buatlah pengimplementasiannya.

'''
'''
Diskon 20% = 0.2
Diskon 15% = 0.15
Rumus setelah diskon = Harga_tiket - Harga_tiket *(diskon)
'''
'''
Input   = Jarak yang akan ditempuh

Proses  = Memasukkan jarak yang ditempuh

Output  = Harga tiket setelah dimasukkan jarak
'''
jarak = int(input("Masukkan Jarak (Km):"))
Harga_tiket = 300000

if jarak >= 301 and jarak <= 400 :
    beli = Harga_tiket - Harga_tiket * 0.2
elif jarak >= 200 and jarak <= 300 :
    beli = Harga_tiket - Harga_tiket * 0.15
elif jarak > 0 and jarak <= 199 :
    beli = Harga_tiket
else :
    print("Tidak ada tiket")

print("Harga Tiket adalah Rp", beli)
