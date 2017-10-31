__author__ = 'WillyLampert'

numbers = []

for i in range(1,1001):
    numbers.append(i**i)

print sum(numbers)