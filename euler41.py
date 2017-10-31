__author__ = 'WillyLampert'

primepandigitals = []

def is_prime(num):
    for x in range(2, num/2):
        if num % x == 0:
            return False
    return True

def is_pandagital(num):
    numstring = str(num)
    for char in numstring:
        if char == '0':
            return False
        if numstring.count(char) > 1:
            return False
        if int(char) > len(numstring):
            return False
    return True

def check_prime_pandigital(num):
    if is_pandagital(num) and is_prime(num):
        return True
    return False

def largest_prime_pandigital(num):
    for x in reversed(range(1000000,num)):
        if check_prime_pandigital(x):
            return x

print largest_prime_pandigital(10000000)

