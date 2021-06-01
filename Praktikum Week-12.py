#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : Saya sendiri

'''
Egi adalah Mahasiswa UKDW, saat ini dia sedang membuat bilangan yang ada pada sebuah list
yang dapat ditambahkan satu sama lain untuk mencapai target yang ingin dicapai, namun apabila
bilangan berada pada posisi yang berdekatan maka bilangan tersebut tidak dapat
dijumlahkan.Apabila bilangan tersebut berdekatan buatlah keluaran Output False, apabila bilangan
tersebut tidak berdekatan maka output akan menghasilkan True Buatlah program rekursif yang dapat
memenuhi syarat tersebut.

'''
'''
INPUT   = - Bilangan yang akan dijumlahkan dalam list

PROSES  = - Program akan membuat perulangan dan menghitung bilangan yang akan dijumlahkan

OUTPUT  = - True/False
'''
def Jarak(iawal, list, iakhir):
    if(iakhir == 0):
        return True

    if(iawal >= len(list)):
       return False

    if(Jarak(iawal+2, list, iakhir - list[iawal])):
        return True

    return Jarak(iawal + 1, list , iakhir)

print(Jarak(0, [5, 7, 11, 4], 16))
