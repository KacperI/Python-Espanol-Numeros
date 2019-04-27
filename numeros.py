import math
import random

small= ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
tens = ["diez","once","doce","trece","catorce","quince","dieciséis","diecisiete","dieciocho","diecinueve"]
big = ["","diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa", "cien"]
twenty = ["veinte","veintiuno","veintidós","veintitrés","veinticuatro","veinticinco","veintiséis","veintisiete","veintiocho","veintinueve"]
huge = ["ciento","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos","mil"]

def divider (number) :
    arr = []
    for x in range(1+int(math.log10(number))):
        arr.append( number % (10 ** (x + 1)) - sum(arr) )
    return arr

def firstPart (array):
    if len(array) < 3:
        array.append(0)
        return ""
    else:
        if array[0] == 0 and array[1] == 0 and array[2]==1:
            return big[10]
        return huge[int(array[2]/100)-1]+" "

def secondPart (array) :
    if array[1] == 0:
        return small[array[0]]
    else:
        if array[1] < 30:
            if array[1] < 20:
                if array[0]!=0:
                    return tens[array[0]]
            else:
                return twenty[array[0]]
        if array[0] != 0:
            return big[int(array[1]/10)]+' y '+small[array[0]]
        else:

            return big[int(array[1]/10)]

def reader (array):
    tmp = firstPart(array)
    tmp += secondPart(array)
    return tmp

points = 0
for x in range(10):
    rand = int(random.random() * 1000)
    print(rand)
    user = input()
    if user == reader(divider(rand)):
        print('Bien\n-----------')
        points += 1
    else:
        print(reader(divider(rand)),'\nIncorrecto\n-----------')
print(points,'/ 10')

user = input()