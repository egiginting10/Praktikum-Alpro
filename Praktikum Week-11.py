#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://www.geeksforgeeks.org/python-program-to-accept-the-strings-which-contains-all-vowels/

'''
Buatlah sebuah program yang dapat mengeluarkan output "Diterima"
apabila didalam kalimat tersebut terdapat huruf vokal "aeiou", apabila
salah satu huruf vokal tidak terdapat dalam kalimat itu maka mengeluarkan
output "Tidak Diterima".

'''
'''
INPUT   = - Kalimat yang akan dicheck

PROSES  = - Fungsi memeriksa apakah string diterima atau tidak dengan mengecek huruf vokal
          - Fungsi mengubah huruf vokal menjadi karakter

OUTPUT  = - String "Diterima" atau "Tidak Diterima"
'''
def check(string):
    string = string.lower()
    vokal = set("aeiou")
    s = set({})
    for char in string:
        if char in vokal:
            s.add(char)
        else:
            pass
    if len(s) == len(vokal):
        print("Diterima")
    else : 
        print("Tidak Diterima")
if __name__ == "__main__" :
    string = "PowerShell All Rights Launcher "
    check(string)