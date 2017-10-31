__author__ = 'WillyLampert'

number = ''

for x in range(0,1000000):
    number += str(x)

print int(number[1]) * int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000])