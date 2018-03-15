import time

def tulo(lista):
    temp = 1
    for i in lista:
        temp *= i
    return temp


def kolmioluku(luku, aloituspiste=1):
    mahdolliset = []
    while aloituspiste ** 2 - 1 < luku:
        temp_summa = []
        temp = aloituspiste
        while tulo(temp_summa) < luku:
            temp_summa.append(temp)
            temp += 1
            if tulo(temp_summa) == luku:
                mahdolliset.append(temp_summa)
        aloituspiste += 1
    return mahdolliset



def prettyPrint(mahdolliset):
    master_temp = []
    for i in mahdolliset:
        temp = ' = '
        for a in i:
            temp += str(a)
            temp += ' * '
        temp = temp[:len(temp) - 3]
        master_temp.append(temp)
    return '\n\t'.join(master_temp)
    # return ','.join(master_temp)

alku = time.time()

for i in range(1000):
    # print(i)
    if i % 1000 == 0:
        loppu = time.time()
        print('\nAika / 1000 itemiä: {}\n\n'.format(loppu - alku))
        alku = loppu
    if not kolmioluku(i):
        continue
    print('{}\t{}\n'.format(i, prettyPrint(kolmioluku(i))))   # prettyprint tapa
