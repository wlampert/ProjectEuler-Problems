__author__ = 'WillyLampert'
import math

numberstring = str(2 ** 1000)
nozeroes = numberstring.replace("0", "")

charlist = list(nozeroes)


def counter(clist):
    valueslist = []
    for i in range(1, 10):
        number_count = clist.count(str(i))
        valueslist.append(number_count * i)
    return sum(valueslist)


print counter(charlist)

