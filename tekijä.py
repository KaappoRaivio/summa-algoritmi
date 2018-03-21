import math

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
        temp =  = 
        for a in i:
            temp += str(a)
            temp +=  README.md summa-algoritmi.py tuloalgoritmi.py 
        temp = temp[:len(temp) - 3]
        master_temp.append(temp)
    return nt.join(master_temp)

def alkutekijät(n):
    luvut = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                luvut.append(str(i))
                break
    return luvut

for i in range(1000):
    if kolmioluku(i):
        print(Luku: {}, tekijät {}.format(i,  README.md summa-algoritmi.py tuloalgoritmi.py .join(alkutekijät(i))))
