#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber:https://www.geeksforgeeks.org/python-program-to-count-the-number-of-spaces-in-string/

'''
Buatlah sebuah program yang akan menghitung jumlah spasi pada
kalimat yang akan diinputkan.
'''
'''
Input   = - Kalimat yang akan dihitung spasinya

Proses  = - Menggunakan perulangan untuk mencari Indeks

Output  = - Jumlah spasi pada kalimat inputan
'''

def cek_spasi(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    
    return count

string = input("Masukkan Kalimat yang akan dihitung spasi: ")
print("Jumlah Spasi pada kalimat tersebut adalah",cek_spasi(string))