__author__ = 'WillyLampert'
import math


def digitalfactorials(num):
    num = str(num)
    numlist = list(num)
    temp = []
    for i in numlist:
        temp.append(math.factorial(int(i)))
    if sum(temp) == int(num):
        return True
    return False


equivalents = []

for i in range(10, 1000000):
    if digitalfactorials(i):
        equivalents.append(i)

print sum(equivalents)

