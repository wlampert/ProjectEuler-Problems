__author__ = 'WillyLampert'

def permutated_multiples(num):
    num2 = num * 2
    num3 = num * 3
    num4 = num * 4
    num5 = num * 5
    num6 = num * 6
    for char in str(num):
        if char not in str(num2):
            return False
        if char not in str(num3):
            return False
        if char not in str(num4):
            return False
        if char not in str(num5):
            return False
        if char not in str(num6):
            return False
    return True


for i in range(1, 1000000):
    j = str(i)
    if j[0] == '1' and permutated_multiples(i):
        print i