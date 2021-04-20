#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : Saya sendiri

'''
Buatlah sebuah program yang inputannya berupa sebuah list dan 
output nya berisi list yang elemennya lebih dari satu (duplicate).
[10,20,30,20,20,30,40,15,-20,-20,95,97,10,97]
'''
'''
INPUT   = - Angka yang akan dimasukkan dalam sebuah list

PROSES  = - Program mencari bilangan yang mempunyai elemen lebih dari satu

OUTPUT  = - List dengan elemen yang lebih dari satu
'''
#Source Code
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

list1 = [10,20,30,20,20,30,40,15,-20,-20,95,97,10,97]
print(Repeat(list1))