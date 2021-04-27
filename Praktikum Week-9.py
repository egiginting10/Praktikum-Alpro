#Nama : Egi Granaldi Ginting
#NIM  : 71200634
#Universitas Kristen Duta Wacana
#Sumber : https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/

'''
Buatlah sebuah program yang dapat menghitung suara/vote didalam
beberapa kandidat dan mencetak nama yang memiliki suara yang lebih besar
'''
'''
Input   = - Nama Kandidat yang akan divote

Proses  = - Membuat dictionary kosong
          - Memasukkan nama kandidat dan menjumlahkan suara dalam kandidat tersebut

Output  = - Nama kandidat dengan jumlah vote terbanyak
'''
from collections import Counter
def winner(input):
    votes = Counter(input)
    dict = {}
    for value in votes.values():
        dict[value] = []
    for (key,value) in votes.items():
        dict[value].append(key)
    maxvote = sorted(dict.keys(),reverse=True)[0]
    if len(dict[maxvote])>1:
        print(sorted(dicti[maxvote])[0])
    else:
        print(dict[maxvote][0])
if __name__ == "__main__":
    input = ['john', 'johnny','jackie','johhny','john','jackie','jamie'
    ,'jamie','john','john','john','johnny','jackie','johnny','johnny']
    winner(input)